import faiss
import numpy as np

def create_faiss_index(embeddings):
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatIP(dimension)
    index.add(np.array(embeddings))
    return index

from embedder import embed_text

def search(index, query, chunks, k=3):
    # Embed the query
    query_embedding = embed_text([query])[0]   # <-- take first element

    # Convert to proper 2D float32 array
    query_vector = np.array([query_embedding]).astype("float32")

    # Search FAISS
    distances, indices = index.search(query_vector, k)

    # Return matched chunks
    return [chunks[i] for i in indices[0]]

