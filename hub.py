
from functools import lru_cache
from transformers import AutoTokenizer, AutoModelForSequenceClassification

MODEL_ID = "cardiffnlp/twitter-roberta-base-sentiment-latest"

@lru_cache(maxsize=1)
def load_hub_model():
    tok = AutoTokenizer.from_pretrained(MODEL_ID)
    mdl = AutoModelForSequenceClassification.from_pretrained(MODEL_ID)
    mdl.eval()
    return tok, mdl
