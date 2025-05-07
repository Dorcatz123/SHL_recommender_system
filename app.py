import streamlit as st
from shl_bot import main  # Your RAG logic

st.set_page_config(page_title="SHL Recommender system", layout="centered")

st.title("🔍 SHL-Recommender system")

st.markdown(
    """
    Enter a question below. The app retrieves relevant SHL test assessments for your need.
    """
)

api_key = st.text_input("🔑 OpenAI API Key", type="password")

# Input form
with st.form("rag_form"):
    user_query = st.text_input("❓ Your question", placeholder="Ask me something...")
    submitted = st.form_submit_button("Get Answer")

if submitted:
    if not api_key:
        st.warning("Please enter your OpenAI API key.")
    elif not user_query:
        st.warning("Please enter a question.")
    with st.spinner("Searching and generating answer..."):
        try:
            answer = main(user_query,api_key)
            st.success("✅ Answer")
            st.write(answer)
        except Exception as e:
            st.error(f"⚠️ Something went wrong: {e}")
