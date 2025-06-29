from langgraph.graph import StateGraph
from langchain_core.runnables import RunnableLambda
from langchain.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone
import google.generativeai as genai
from typing import TypedDict, List

GOOGLE_API_KEY = "AIzaSyA8-Q1tO01v3RN3OW_VXezySZ9EVxIN4Ho"
PINECONE_API_KEY = "pcsk_SgnNc_9ik7komL5utGusr14w9sRaUTf3byjRwHhPiyQuXmtAKJVLpu9U3Yof5cTbEryHF"
INDEX_NAME = "violation-index"

genai.configure(api_key=GOOGLE_API_KEY)

class GraphState(TypedDict):
    question: str
    docs: List[str]
    answer: str

def check_question_node(state: GraphState) -> GraphState:
    if not state.get("question", "").strip():
        raise ValueError("Empty alert message.")
    return state

def retrieve_documents_node(state: GraphState) -> GraphState:
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=GOOGLE_API_KEY
    )
    pc = Pinecone(api_key=PINECONE_API_KEY)
    index = pc.Index(INDEX_NAME)

    vector_store = PineconeVectorStore(
        index=index,
        embedding=embeddings,
        text_key="text"
    )
    docs = vector_store.similarity_search(state["question"], k=4)
    state["docs"] = docs
    return state

def generate_answer_node(state: GraphState) -> GraphState:
    context = "\n\n".join([doc.page_content for doc in state["docs"]])

    prompt = PromptTemplate(
        template="""
Use the context below to answer whether the alert message violates company policy or SLA.

If the answer is in the document, cite the clause or section.

Context:
{context}

Alert:
{question} 

Answer:""",
        input_variables=["context", "question"]
    )

    model = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.2,
        google_api_key=GOOGLE_API_KEY
    )

    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    result = chain({"input_documents": state["docs"], "question": state["question"]})
    state["answer"] = result["output_text"]
    return state

# Build graph
graph = StateGraph(GraphState)
graph.add_node("check_question", RunnableLambda(check_question_node))
graph.add_node("retrieve_documents", RunnableLambda(retrieve_documents_node))
graph.add_node("generate_answer", RunnableLambda(generate_answer_node))
graph.set_entry_point("check_question")
graph.add_edge("check_question", "retrieve_documents")
graph.add_edge("retrieve_documents", "generate_answer")
graph.set_finish_point("generate_answer")
langgraph_chain = graph.compile()

def check_violation(question: str) -> str:
    state: GraphState = {"question": question}
    result = langgraph_chain.invoke(state)
    return result["answer"]
