
# Sentiment AI Suite — Pro Free Edition (Streamlit · Hugging Face)

**Free, no API keys.** Uses `cardiffnlp/twitter-roberta-base-sentiment-latest` from the Hugging Face Hub.  
Streamlit UI supports **single text** analysis and **CSV batch** analysis.

## Run on Hugging Face Spaces
- Create a Space (type: **Streamlit**)
- Upload this repo (or extract the ZIP)
- Entry file: `app.py` → Click **Run**

## Local / Colab
```bash
pip install -r requirements.txt
streamlit run app.py
```
- CSV format: one column named `text` (UTF-8)

## Outputs
- Labels: `Negative`, `Neutral`, `Positive`
- For CSV batch: `text, label, negative, neutral, positive`
