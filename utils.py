from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader

import functools

# Cache the embeddings model to avoid reloading it
@functools.lru_cache(maxsize=1)
def get_embeddings_model():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={'device': 'cpu'}  # Force CPU, avoids GPU meta tensor issues
    )

# Load and split PDF into chunks
def load_and_split_pdf(pdf_file):
    loader = PyPDFLoader(pdf_file)
    documents = loader.load()
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,  # smaller chunks
        chunk_overlap=100  # more overlap to catch related lines
    )
    docs = splitter.split_documents(documents)
    return docs

# Create FAISS vectorstore
def create_vectorstore(docs):
    embeddings = get_embeddings_model()  # use cached model
    vectorstore = FAISS.from_documents(docs, embeddings)
    return vectorstore
