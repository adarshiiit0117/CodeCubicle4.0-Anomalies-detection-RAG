import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone, ServerlessSpec
from Violates import check_violation

GOOGLE_API_KEY = "AIzaSyA8-Q1tO01v3RN3OW_VXezySZ9EVxIN4Ho"
PINECONE_API_KEY = "pcsk_SgnNc_9ik7komL5utGusr14w9sRaUTf3byjRwHhPiyQuXmtAKJVLpu9U3Yof5cTbEryHF"
INDEX_NAME = "violation-index"

# Initialize Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)

# Create index if it doesn't exist
if INDEX_NAME not in [i['name'] for i in pc.list_indexes()]:
    pc.create_index(
        name=INDEX_NAME,
        dimension=768,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )

index = pc.Index(INDEX_NAME)

# Initialize embeddings
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=GOOGLE_API_KEY
)

# Streamlit UI
st.title("PDF Violation Checker")
user_question = st.text_input("Enter an alert or question to check for violations")
uploaded_files = st.file_uploader(" Upload your PDFs", accept_multiple_files=True)

if uploaded_files:
    raw_text = ""
    for pdf in uploaded_files:
        reader = PdfReader(pdf)
        for page in reader.pages:
            text = page.extract_text()
            if text:
                raw_text += text

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    texts = text_splitter.split_text(raw_text)

    vector_store = PineconeVectorStore(
        index=index,
        embedding=embeddings,
        text_key="text"
    )
    vector_store.add_texts(texts=texts, metadatas=[{"text": t} for t in texts])

    st.success(" Texts embedded and saved to Pinecone index.")

if user_question:
    try:
        response = check_violation(user_question)
        st.write(" Violation Check Result:", response)
    except Exception as e:
        st.error(f"Error during violation check: {e}")
