from src.retrieval.vector_store import get_chroma_client, get_collection

client = get_chroma_client()
collection = get_collection(client)


print("Collection created successfully.")
print("Collection name:", collection.name)
print("Number of documents:", collection.count())