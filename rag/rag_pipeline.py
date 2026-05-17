from doct_loader import load_pdf
from chunker import chunk_text
from embedder import embed_text
from vector_store import create_faiss_index, search
from generator import generate_answer

print("Starting script...")

# Load document
text = load_pdf("notes.pdf")

# Chunk
chunks = chunk_text(text)

# Embed
embeddings = embed_text(chunks)

# Create index
index = create_faiss_index(embeddings)

print("Entering interactive mode...")

def ask_question(question):
    # Search relevant chunks
    results = search(index, question, chunks)

    # Generate answer
    answer = generate_answer(question, results)

    return answer

if __name__ == "__main__":
    while True:
        question = input("Ask: ")

        if question.lower() == "exit":
            break

        answer = ask_question(question)
        print("\nAnswer:", answer)
        print("-" * 50)
