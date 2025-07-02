
import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
import os
import tempfile

from data_loader import load_and_embed_documents
from chat import create_rag_chain

st.set_page_config(page_title="Chat with Documents", page_icon="🤖")

st.title("Chat with your documents 🤖")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "rag_chain" not in st.session_state:
    st.session_state.rag_chain = None

with st.sidebar:
    st.header("Upload your document")
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    if uploaded_file:
        with st.spinner("Processing document..."):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                tmp_file.write(uploaded_file.getvalue())
                tmp_file_path = tmp_file.name
            
            vectordb = load_and_embed_documents(pdf_path=tmp_file_path)
            st.session_state.rag_chain = create_rag_chain(vectordb)
            os.remove(tmp_file_path)
            st.success("Document processed successfully!")

for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.markdown(message.content)
    else:
        with st.chat_message("AI"):
            st.markdown(message.content)

user_q = st.chat_input("Ask me a question about the document...")

if user_q:
    if st.session_state.rag_chain:
        st.session_state.chat_history.append(HumanMessage(content=user_q))
        with st.chat_message("Human"):
            st.markdown(user_q)

        with st.spinner("Thinking..."):
            result = st.session_state.rag_chain.invoke(
                {"input": user_q, "chat_history": st.session_state.chat_history}
            )
            answer = result["answer"]

        st.session_state.chat_history.append(AIMessage(content=answer))
        with st.chat_message("AI"):
            st.markdown(answer)
    else:
        st.warning("Please upload a document first.")
