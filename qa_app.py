import streamlit as st
from transformers import pipeline
from langchain.chains import RetrievalQA
from langchain_community.llms import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from utils import load_and_split_pdf, create_vectorstore

# Initialize Hugging Face model
@st.cache_resource
def load_qa_pipeline():
    hf_pipeline = pipeline(
        "text2text-generation",  # better for QA tasks
        model="google/flan-t5-small",
        max_length=200,
        temperature=0.7
    )
    llm = HuggingFacePipeline(pipeline=hf_pipeline)
    return llm

# Set up the custom prompt template
prompt = PromptTemplate(
    template="""
Answer the following question using ONLY the provided context. 
If the answer is not in the context, say "I don't know." 
Be concise and avoid including unrelated information.

Context:
{context}

Question: {question}

Answer:""",
    input_variables=["context", "question"]
)

# Streamlit app UI
st.title(" Document Question Answering System")
st.write("Upload a PDF and ask questions about its content.")

# File uploader
uploaded_file = st.file_uploader(" Upload your PDF", type="pdf")

if uploaded_file:
    # Save uploaded PDF
    with open("uploaded.pdf", "wb") as f:
        f.write(uploaded_file.read())
    
    st.success(" PDF uploaded successfully!")
    
    # Process PDF and create QA system
    with st.spinner(" Processing document..."):
        docs = load_and_split_pdf("uploaded.pdf")
        vectorstore = create_vectorstore(docs)
        retriever = vectorstore.as_retriever()
        retriever.search_kwargs["k"] = 3  # fetch top 3 relevant chunks
        
        # Load model and create QA chain
        llm = load_qa_pipeline()
        qa_chain = load_qa_chain(
            llm=llm,
            chain_type="stuff",
            prompt=prompt
        )

    # Chat interface
    st.subheader(" Ask questions about your document")
    question = st.text_input("Enter your question")
    if st.button("Get Answer"):
        if question.strip() != "":
            with st.spinner(" Generating answer..."):
                # Retrieve relevant context
                docs = retriever.get_relevant_documents(question)
                # Run QA chain with both context and question
                answer = qa_chain.run({
                    "input_documents": docs,
                    "question": question
                })
                st.success(answer)
        else:
            st.warning(" Please enter a question.")
 