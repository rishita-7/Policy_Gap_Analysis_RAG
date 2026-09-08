<img width="155" height="236" alt="image" src="https://github.com/user-attachments/assets/1cbf7003-9987-4324-871d-4a5257e28df2" /># Policy Gap Analysis RAG

A Retrieval-Augmented Generation (RAG) based cybersecurity policy gap analyzer.

## Objective

This project implements a RAG-based approach for analyzing organizational cybersecurity policies against the NIST Cybersecurity Framework.

This is a separate implementation from my earlier NLP and keyword-matching based Policy Gap Analyzer.

## Architecture

```mermaid
flowchart TD
    A[Policy Document] --> B[Document Processing]
    B --> C[Chunking]
    C --> D[Embeddings]
    D --> E[Vector Database]
    E --> F[Semantic Retrieval]
    F --> G[Relevant NIST Context]
    G --> H[LLM]
    H --> I[Evidence-Based Gap Analysis]
```


## Tech Stack

- Python
- PyMuPDF
- Sentence Transformers
- ChromaDB
- Streamlit
- LLM

## Project Status

🚧 Under Development

### Progress

- [x] Repository setup
- [x] NIST document ingestion
- [x] Document chunking
- [x] Embeddings
- [x] Vector database
- [ ] Semantic retrieval
- [ ] LLM integration
- [ ] Evidence-based gap analysis
- [ ] Streamlit interface
- [ ] Evaluation against NLP approach
