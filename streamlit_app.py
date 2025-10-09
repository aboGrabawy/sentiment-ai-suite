
import io
import pandas as pd
import torch
import torch.nn.functional as F
import streamlit as st
from .theme import inject_base_css, brand_header, prob_bar
from ..utils.hub import load_hub_model

LABELS = ["Negative", "Neutral", "Positive"]

def infer_text(text: str):
    tok, mdl = load_hub_model()
    inp = tok(text, return_tensors="pt", truncation=True, padding=True, max_length=256)
    with torch.no_grad():
        logits = mdl(**inp).logits
        probs = F.softmax(logits, dim=-1).squeeze().tolist()
    idx = int(torch.tensor(probs).argmax())
    return LABELS[idx], probs

def infer_df(df: pd.DataFrame):
    tok, mdl = load_hub_model()
    texts = df["text"].astype(str).tolist()
    outs = []
    for t in texts:
        inp = tok(t, return_tensors="pt", truncation=True, padding=True, max_length=256)
        with torch.no_grad():
            logits = mdl(**inp).logits
            probs = F.softmax(logits, dim=-1).squeeze().tolist()
        idx = int(torch.tensor(probs).argmax())
        outs.append((LABELS[idx], *probs))
    out_df = df.copy()
    out_df["label"] = [o[0] for o in outs]
    out_df["negative"] = [o[1] for o in outs]
    out_df["neutral"]  = [o[2] for o in outs]
    out_df["positive"] = [o[3] for o in outs]
    return out_df

def main():
    inject_base_css()
    brand_header("Sentiment AI Suite — Pro Free Edition",
                 "Free Hugging Face inference • Streamlit UI • CSV batch support")
    st.write("")

    tab1, tab2 = st.tabs(["🔎 Single Text", "📁 CSV Batch"])

    with tab1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        txt = st.text_area("Enter text", "The product onboarding was smooth and the team was very helpful!")
        run = st.button("Analyze", type="primary", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

        if run and txt.strip():
            label, probs = infer_text(txt)
            st.success(f"Prediction: **{label}**")
            prob_bar("Negative", probs[0] * 100)
            prob_bar("Neutral",  probs[1] * 100)
            prob_bar("Positive", probs[2] * 100)

    with tab2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.write("Upload a CSV file with a **text** column.")
        upl = st.file_uploader("CSV file", type=["csv"], accept_multiple_files=False)
        do = st.button("Run Batch", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

        if do and upl is not None:
            try:
                df = pd.read_csv(upl)
            except Exception as e:
                st.error(f"Failed to read CSV: {e}")
                return
            if "text" not in df.columns:
                st.error("CSV must contain a 'text' column.")
                return
            with st.spinner("Running batch inference..."):
                out_df = infer_df(df)
            st.success("Done.")
            st.dataframe(out_df.head(50))
            # Download button
            buf = io.StringIO()
            out_df.to_csv(buf, index=False)
            st.download_button("Download Results CSV", buf.getvalue().encode("utf-8"),
                               file_name="sentiment_results.csv", mime="text/csv")

if __name__ == "__main__":
    main()
