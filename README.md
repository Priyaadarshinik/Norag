## Norag - Personal notes RAG chatbot
A Retrieval-Augmented Generation (RAG) based chatbot that allows users to query PDF documents using semantic search and Large Language Models (LLMs).
The system retrieves the most relevant document chunks using vector similarity search and generates context-aware responses grounded only in the uploaded document content.

## Features

- PDF document ingestion
- Text chunking with overlap
- Semantic similarity search
- Transformer-based embeddings
- LLM-powered answer generation
- Hallucination reduction using context grounding
- Terminal-based interactive Q&A
-  Fast retrieval using FAISS

## Tech Stack

Programming Language : Python
Libraries & Frameworks: Transformers, Sentence Transformers, PyTorch, NumPy, FAISS. PyPDF
Embedding Model: all-MiniLM-L6-v2
Language Model: TinyLlama-1.1B-Chat-v1.0

## Concepts Used

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Vector Embeddings
- Cosine Similarity
- Prompt Engineering
- Transformer Architecture
- Context Injection
- Similarity Retrieval

## Workflow

1. Load PDF document
2. Extract text from PDF
3. Split text into chunks
4. Convert chunks into embeddings
5. Store embeddings in FAISS index
6. Accept user query
6. Retrieve top-k relevant chunks
7. Send retrieved context to LLM
8. Generate grounded answer

## Installation

Clone Repository
```
git clone <your-repo-link>
cd personal_rag
```
Install Dependencies
```
pip install torch transformers sentence-transformers faiss-cpu pypdf numpy
```
Running the Project

Place your PDF file in the project folder.

Run:
```
python rag_pipeline.py
```
Example:
```
Ask: What does RAG stand for?
```
Output:
```
RAG stands for Retrieval Augmented Generation.
```
## Sample Prompt

You are a document assistant.
Answer ONLY from the provided context.
If the answer is not available in the document,
say "I don't have enough information in the provided documents."

## Future Improvements

- Add multi-document support
- Implement query rewriting
- Add reranking models
- Add source citation display
- Build web interface
- Add persistent vector database
- Experiment with hybrid search
