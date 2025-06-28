# main.py

import os
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from violates import check_violation

# ----------------- UI -----------------
st.title("PDF Violation Checker")
user_question = st.text_input("Enter an alert or question to check for violations")
uploaded_files = st.file_uploader("Upload your PDFs", accept_multiple_files=True)

# ----------------- Embeddings -----------------
GOOGLE_API_KEY = "AIzaSyA8-Q1tO01v3RN3OW_VXezySZ9EVxIN4Ho"
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=GOOGLE_API_KEY
)

# ----------------- PDF Processing -----------------
INDEX_PATH = "faiss_index"

if uploaded_files:
    raw_text = ""
    for pdf in uploaded_files:
        reader = PdfReader(pdf)
        for page in reader.pages:
            text = page.extract_text()
            if text:
                raw_text += text

    # Split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    texts = text_splitter.split_text(raw_text)

    # Create FAISS index
    docsearch = FAISS.from_texts(texts, embeddings)

    # Save FAISS index to disk using FAISS' built-in method
    docsearch.save_local(INDEX_PATH)

# ----------------- Violation Check -----------------
if user_question:
    try:
        response = check_violation(user_question)
        st.write("Violation Check Result:", response)
    except Exception as e:
        st.error(f"Error during violation check: {e}")
