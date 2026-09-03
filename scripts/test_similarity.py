from src.ingestion.document_loader import load_pdf
from src.ingestion.chunker import create_chunks
from src.retrieval.embedding_model import load_embedding_model
import numpy as np

from sklearn.metrics.pairwise import cosine_similarity


PDF_PATH = "data/raw/framework/nist_csf_2.0.pdf"


# -----------------------------
# 1. Load and chunk NIST
# -----------------------------

pages = load_pdf(PDF_PATH)
chunks = create_chunks(pages)

texts = [chunk["text"] for chunk in chunks]

print("Total chunks:", len(texts))


# -----------------------------
# 2. Load BGE-M3
# -----------------------------

model = load_embedding_model()


# -----------------------------
# 3. Loading NIST embeddings
# -----------------------------

print("\nLoading saved NIST embeddings...")

nist_embeddings = np.load(
    "data/processed/nist_embeddings.npy"
)

print("NIST embeddings shape:", nist_embeddings.shape)


# -----------------------------
# 4. Create a query
# -----------------------------

query = "Users must authenticate before accessing company systems."


# -----------------------------
# 5. Generate query embedding
# -----------------------------

query_embedding = model.encode([query])

print("Query embedding shape:", query_embedding.shape)


# -----------------------------
# 6. Calculate cosine similarity
# -----------------------------

similarities = cosine_similarity(
    query_embedding,
    nist_embeddings
)[0]


# -----------------------------
# 7. Get top 5 results
# -----------------------------

top_indices = similarities.argsort()[::-1][:5]


print("\n========== TOP 5 RESULTS ==========\n")

for rank, index in enumerate(top_indices, start=1):

    print(f"Rank: {rank}")
    print(f"Similarity: {similarities[index]:.4f}")
    print(f"Chunk ID: {chunks[index]['metadata']['chunk_id']}")
    print(f"Subcategory: {chunks[index]['metadata']['subcategory_id']}")
    print(f"Text: {chunks[index]['text']}")
    print("-" * 80)