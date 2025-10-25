# utils/sentiment.py
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import numpy as np

# Load FinBERT model
tokenizer = AutoTokenizer.from_pretrained("yiyanghkust/finbert-tone")
model = AutoModelForSequenceClassification.from_pretrained("yiyanghkust/finbert-tone")

def analyze_sentiment(text):
    """
    Analyze sentiment of a single text using FinBERT.
    
    Args:
        text (str): Input text (news headline)
        
    Returns:
        str: "Positive", "Neutral", or "Negative"
    """
    inputs = tokenizer(text, return_tensors="pt", truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
    
    scores = outputs.logits[0].numpy()
    label_idx = np.argmax(scores)
    labels = ["neutral", "positive", "negative"]
    return labels[label_idx].capitalize()

def analyze_news_list(news_list):
    """
    Analyze sentiment for a list of news headlines.
    
    Args:
        news_list (list of dict): List of {"title": ..., "link": ...}
        
    Returns:
        list of dict: Each dict has title, link, sentiment
    """
    analyzed = []
    for news in news_list:
        sentiment = analyze_sentiment(news["title"])
        analyzed.append({**news, "sentiment": sentiment})
    return analyzed
