from langchain_community.llms import Ollama
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import (
    create_history_aware_retriever,
    create_retrieval_chain,
)
from langchain.chains.combine_documents import create_stuff_documents_chain

from app.config import LLM_MODEL, CONDENSE_PROMPT_SYSTEM, ANSWER_PROMPT_SYSTEM

def create_rag_chain(vectordb):
    llm = Ollama(model=LLM_MODEL)

    CONDENSE_PROMPT = ChatPromptTemplate.from_messages(
        [
            ("system", CONDENSE_PROMPT_SYSTEM),
            MessagesPlaceholder("chat_history"),
            ("user", "{input}"),
        ]
    )

    ANSWER_PROMPT = ChatPromptTemplate.from_messages(
        [
            ("system", ANSWER_PROMPT_SYSTEM),
            MessagesPlaceholder("chat_history"),
            ("system", "Relevant context:\n{context}"),
            ("user", "{question}"),
        ]
    )

    history_aware_retriever = create_history_aware_retriever(
        llm,
        vectordb.as_retriever(search_kwargs={"k": 4}),
        prompt=CONDENSE_PROMPT,
    )

    combine_chain = create_stuff_documents_chain(llm, ANSWER_PROMPT)

    rag_chain = create_retrieval_chain(
        history_aware_retriever,
        combine_chain,
    )

    return rag_chain
