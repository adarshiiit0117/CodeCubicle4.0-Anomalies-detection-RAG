# violates.py

from langgraph.graph import StateGraph
from langchain_core.runnables import RunnableLambda
from langchain_community.vectorstores import FAISS  
from langchain.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
import google.generativeai as genai
from typing import TypedDict, List

# ----------------- Setup -----------------
GOOGLE_API_KEY = "AIzaSyA8-Q1tO01v3RN3OW_VXezySZ9EVxIN4Ho"
INDEX_PATH = "faiss_index"
genai.configure(api_key=GOOGLE_API_KEY)

# ----------------- Schema -----------------
class GraphState(TypedDict):
    question: str
    docs: List[str]
    answer: str

# ----------------- Nodes -----------------
def check_question_node(state: GraphState) -> GraphState:
    if not state.get("question", "").strip():
        raise ValueError("Empty alert message.")
    return state

def retrieve_documents_node(state: GraphState) -> GraphState:
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=GOOGLE_API_KEY)
    db = FAISS.load_local(INDEX_PATH, embeddings, allow_dangerous_deserialization=True)
    docs = db.similarity_search(state["question"])
    state["docs"] = docs
    return state

def generate_answer_node(state: GraphState) -> GraphState:
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
    model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.2, google_api_key=GOOGLE_API_KEY)
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    result = chain({"input_documents": state["docs"], "question": state["question"]})
    state["answer"] = result["output_text"]
    return state

# ----------------- Graph -----------------
graph = StateGraph(GraphState)  

graph.add_node("check_question", RunnableLambda(check_question_node))
graph.add_node("retrieve_documents", RunnableLambda(retrieve_documents_node))
graph.add_node("generate_answer", RunnableLambda(generate_answer_node))

graph.set_entry_point("check_question")
graph.add_edge("check_question", "retrieve_documents")
graph.add_edge("retrieve_documents", "generate_answer")
graph.set_finish_point("generate_answer")

langgraph_chain = graph.compile()

# ----------------- Entry -----------------
def check_violation(question: str) -> str:
    state: GraphState = {"question": question}
    result = langgraph_chain.invoke(state)
    return result["answer"]
