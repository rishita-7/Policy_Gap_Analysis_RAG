from sentence_transformers import SentenceTransformer

#Loading the embedding model
def load_embedding_model():
    model = SentenceTransformer("BAAI/bge-m3")
    return model


def generate_embeddings(model,texts):
    embeddings = model.encode(texts, show_progress_bar=True)
    return embeddings