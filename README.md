# 📄 Document Question Answering System

A **Streamlit app** that allows users to upload a PDF document and ask questions about its content using **Hugging Face Transformers** and **LangChain**. The system retrieves the most relevant information from the PDF and generates concise, context-aware answers.

---

##  Objective
The main objective of this project is to create an **intelligent document assistant** that enables users to interact with their documents conversationally. Instead of manually searching through lengthy PDFs, users can directly ask questions and get precise answers powered by natural language processing (NLP).

---

##  Purpose
- To **simplify information retrieval** from large and complex PDF files.  
- To **demonstrate the integration** of Hugging Face models and LangChain for building retrieval-augmented generation (RAG) systems.  
- To build a lightweight and **user-friendly interface** using Streamlit for seamless interaction.  

---

##  Use Cases
 **Students & Researchers**: Quickly extract key insights from academic papers, theses, or research reports.  

 **Legal Professionals**: Ask questions about lengthy contracts or legal documents and retrieve only relevant sections.  

 **Business Analysts**: Get instant answers from business reports, financial statements, or market research PDFs.  

 **Healthcare Professionals**: Summarize and query medical reports or patient history PDFs.  

 **Anyone** dealing with large volumes of textual data in PDFs and wants **instant answers** without manual scanning.

---

## Technologies Used
|  Tool/Library         |  Purpose                                      |
|--------------------------|------------------------------------------------|
| **Python**               | Core programming language                     |
| **Streamlit**            | Web interface for uploading PDFs and asking questions |
| **Hugging Face Transformers** | Pre-trained NLP model (`google/flan-t5-small`) for generating answers |
| **LangChain**            | Document processing and retrieval-augmented generation |
| **PyPDF2**               | Reading and splitting PDF documents           |
| **FAISS**                | Vector database for semantic search           |
| **SentenceTransformers** | Encoding text chunks into vector embeddings   |

---

##  How It Works
1.  Upload a PDF document.  
2.  The system splits the PDF into smaller chunks and indexes them.  
3.  Ask your question in natural language.  
4.  The app retrieves relevant chunks and uses a language model to generate the answer.  

---

##  Demo
Here’s how the app looks:  

![Document QA Demo](images/screenshot.png)

---

## 🖥 Run Locally
1. Clone this repository:
   ```bash
   git clone https://github.com/<Rushikesh696>/document-qa-app.git
   cd document-qa-app
