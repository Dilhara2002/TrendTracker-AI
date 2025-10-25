# utils/data_fetcher.py
import yfinance as yf
import feedparser

def fetch_stock_data(symbol, period="30d"):
    try:
        data = yf.Ticker(symbol).history(period=period)
        return data
    except Exception as e:
        print(f"Error fetching stock data: {e}")
        return None

def fetch_news(symbol):
    rss_url = f"https://finance.yahoo.com/rss/headline?s={symbol}"
    try:
        feed = feedparser.parse(rss_url)
        news_list = [{"title": entry.title, "link": entry.link} for entry in feed.entries]
        return news_list
    except Exception as e:
        print(f"Error fetching news: {e}")
        return []
