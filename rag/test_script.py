from rag_pipeline import ask_question

while True:
    q = input("Ask: ")
    if q.lower() == "exit":
        break
    print(ask_question(q))
