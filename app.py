import streamlit as st
from shl_bot import main  # Your RAG logic

st.set_page_config(page_title="RAG Demo", layout="centered")

st.title("🔍 Retrieval-Augmented Generation Demo")

st.markdown(
    """
    Enter a question below. The app retrieves relevant context and generates an answer using OpenAI + vector DB.
    """
)

# Input form
with st.form("rag_form"):
    user_query = st.text_input("❓ Your question", placeholder="Ask me something...")
    submitted = st.form_submit_button("Get Answer")

if submitted and user_query:
    with st.spinner("Searching and generating answer..."):
        try:
            answer = rag_answer(user_query)
            st.success("✅ Answer")
            st.write(answer)
        except Exception as e:
            st.error(f"⚠️ Something went wrong: {e}")
