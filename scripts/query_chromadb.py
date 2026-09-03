from sentence_transformers import SentenceTransformer

from src.retrieval.vector_store import (
    get_chroma_client,
    get_collection
)


MODEL_NAME = "BAAI/bge-m3"


# Load embedding model
model = SentenceTransformer(MODEL_NAME)


# Connect to ChromaDB
client = get_chroma_client()
collection = get_collection(client)


# Example policy statement
query = "Users must authenticate before accessing company systems."


# Convert query into an embedding
query_embedding = model.encode([query])


# Search ChromaDB
results = collection.query(
    query_embeddings=query_embedding.tolist(),
    n_results=5
)


print("\n========== TOP 5 RESULTS ==========\n")


for i in range(5):

    print(f"Rank: {i + 1}")

    print(
        "Distance:",
        results["distances"][0][i]
    )

    print(
        "Subcategory:",
        results["metadatas"][0][i]["subcategory_id"]
    )

    print(
        "Text:",
        results["documents"][0][i]
    )

    print("-" * 80)