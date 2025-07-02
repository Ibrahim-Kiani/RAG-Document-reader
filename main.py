from langchain_core.messages import HumanMessage, AIMessage

from app.data_loader import load_and_embed_documents
from app.chat import create_rag_chain

def main():
    vectordb = load_and_embed_documents()
    rag_chain = create_rag_chain(vectordb)

    chat_history = []

    print("🗨️  Ask me about the LangChain paper (type 'exit' to quit)")
    while True:
        user_q = input("You: ")
        if user_q.lower() in {"exit", "quit"}:
            break

        result = rag_chain.invoke(
            {"input": user_q, "question": user_q, "chat_history": chat_history}
        )

        answer = result["answer"]
        print("🤖", answer)

        chat_history.extend(
            [HumanMessage(content=user_q), AIMessage(content=answer)]
        )

if __name__ == "__main__":
    main()
