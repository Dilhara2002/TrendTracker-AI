# app.py
import streamlit as st
from utils.data_fetcher import fetch_stock_data, fetch_news
from utils.sentiment import analyze_news_list
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="TrendTracker AI", layout="wide")
st.title("📈 TrendTracker AI")

# --- Sidebar ---
st.sidebar.header("Settings")
stock_symbol = st.sidebar.text_input("Enter Stock Symbol:", "AAPL")
days = st.sidebar.slider("Days of History:", 7, 180, 30)

# --- Fetch Stock Data ---
st.subheader(f"Stock Price Data: {stock_symbol}")
stock_data = fetch_stock_data(stock_symbol, period=f"{days}d")

if not stock_data.empty:
    st.line_chart(stock_data["Close"])
else:
    st.warning("No stock data found.")

# --- Fetch News ---
st.subheader("Latest Financial News")
news_list = fetch_news(stock_symbol)
if news_list:
    analyzed_news = analyze_news_list(news_list)
    
    # Convert to DataFrame for display
    df_news = pd.DataFrame(analyzed_news)
    df_news = df_news[["title", "sentiment", "link"]]
    df_news["title"] = df_news["title"].apply(lambda x: f"[{x}](#)")
    st.dataframe(df_news)
else:
    st.warning("No news found.")

# --- Sentiment Summary ---
if news_list:
    st.subheader("Market Sentiment Overview")
    sentiment_counts = df_news["sentiment"].value_counts()
    st.bar_chart(sentiment_counts)
