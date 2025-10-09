import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="Sentiment AI Suite", page_icon="🧠", layout="centered")

st.title("💬 Sentiment AI Suite")
st.write("Analyze sentiment of any text using a RoBERTa transformer model.")

# بارگذاری مدل
@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment-latest")

analyzer = load_model()

text = st.text_area("✍️ Enter your text here:")

if st.button("Analyze Sentiment"):
    if text.strip():
        with st.spinner("Analyzing..."):
            result = analyzer(text)[0]
            st.success(f"Label: {result['label']} — Confidence: {result['score']:.2f}")
    else:
        st.warning("Please enter some text first.")