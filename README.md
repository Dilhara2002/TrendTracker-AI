# 📈 TrendTracker AI

**TrendTracker AI** is an AI-powered web app that helps users analyze stock market trends and understand the market mood using real-time financial data and sentiment analysis.  
It combines live stock prices, recent financial news, and **FinBERT** (a financial NLP model) to show whether the market sentiment is **positive**, **neutral**, or **negative**.

---

## 🚀 Features

✅ Fetch real-time stock price data using **yfinance**  
✅ Display interactive stock price charts  
✅ Get recent finance news headlines (from **Yahoo Finance RSS**)  
✅ Analyze each headline’s sentiment using **FinBERT** (free Hugging Face model)  
✅ 100% free to build, run, and deploy  

---

## 🧰 Tech Stack

| Layer | Technology | Purpose |
|-------|-------------|----------|
| **Frontend** | [Streamlit](https://streamlit.io/) | Interactive dashboard |
| **Backend** | Python | Core logic & AI integration |
| **Stock Data** | [yfinance](https://pypi.org/project/yfinance/) | Real-time stock market data |
| **News Feed** | [feedparser](https://pypi.org/project/feedparser/) | Financial news RSS |
| **AI Model** | [FinBERT](https://huggingface.co/yiyanghkust/finbert-tone) | Sentiment analysis |
| **Visualization** | Streamlit Charts / Matplotlib | Graphs & insights |
| **Hosting** | Streamlit Cloud / Hugging Face Spaces | Free deployment |

---

## 📦 Project Structure

