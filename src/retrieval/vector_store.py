import chromadb


DB_PATH = "data/vectorstore"


def get_chroma_client():
    """
    Create a persistent ChromaDB client.
    """

    client = chromadb.PersistentClient(
        path=DB_PATH
    )

    return client


def get_collection(client):
    """
    Get or create the NIST CSF 2.0 collection.
    """

    collection = client.get_or_create_collection(
        name="nist_csf_2_0"
    )

    return collection

def add_documents(collection, chunks, embeddings):
    """
    Add NIST CSF chunks, embeddings, and metadata to ChromaDB.
    """

    documents = [chunk["text"] for chunk in chunks]

    metadatas = [chunk["metadata"] for chunk in chunks]

    ids = [
        f"nist_{chunk['metadata']['chunk_id']}"
        for chunk in chunks
    ]

    collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings.tolist(),
        metadatas=metadatas
    )