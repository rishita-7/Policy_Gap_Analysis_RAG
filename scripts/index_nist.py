import numpy as np

from src.ingestion.document_loader import load_pdf
from src.ingestion.chunker import create_chunks
from src.retrieval.vector_store import (
    get_chroma_client,
    get_collection,
    add_documents
)


PDF_PATH = "data/raw/framework/nist_csf_2.0.pdf"
EMBEDDINGS_PATH = "data/processed/nist_embeddings.npy"


# Load and chunk the NIST document
pages = load_pdf(PDF_PATH)
chunks = create_chunks(pages)

print("Total chunks:", len(chunks))


# Load previously generated embeddings
embeddings = np.load(EMBEDDINGS_PATH)

print("Embeddings shape:", embeddings.shape)


# Connect to ChromaDB
client = get_chroma_client()
collection = get_collection(client)


# Prevent accidental duplicate indexing
if collection.count() > 0:

    print("Collection already contains documents.")
    print("Current document count:", collection.count())

else:

    add_documents(
        collection,
        chunks,
        embeddings
    )

    print("NIST documents indexed successfully.")


print("Final document count:", collection.count())