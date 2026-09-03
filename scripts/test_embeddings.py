from src.ingestion.document_loader import load_pdf
from src.ingestion.chunker import create_chunks
from src.retrieval.embedding_model import load_embedding_model, generate_embeddings
import numpy as np

PDF_PATH = "data/raw/framework/nist_csf_2.0.pdf"
#Loading Pdf
pages = load_pdf(PDF_PATH)
print(f"Total pages: {len(pages)}")

# Creating Chunks
chunks = create_chunks(pages)
texts = [chunk["text"] for chunk in chunks]
print("Total chunks:", len(texts))

# Load Embedding Model
model = load_embedding_model()

# Generating Embeddings for Chunks
print("Generating embeddings for chunks...")
embeddings = generate_embeddings(model, texts)
np.save(
    "data/processed/nist_embeddings.npy",
    embeddings
)
print("Embeddings generated for all chunks.")
print("Number of embeddings:", len(embeddings))
print("Dimension of each embedding:", len(embeddings[0]))
