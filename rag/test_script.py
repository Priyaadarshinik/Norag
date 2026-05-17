from rag_pipeline import ask_question

while True:
    q = input("Ask: ")
    if q.lower() == "exit":
        break
    answer, sources = ask_question(q)
    print("\nAnswer:",answer)
    print("\nSources:",len(sources), "chunks used")
    print("-" * 40)
    # print(ask_question(q))
