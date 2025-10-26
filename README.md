
# 📈 TrendTracker AI

**TrendTracker AI** is an AI-powered web application designed to help users track stock market trends and understand market sentiment in real time. By combining live stock prices, financial news, and AI-driven sentiment analysis, it provides actionable insights for traders, investors, and finance enthusiasts.

---

## 🚀 Features

* **Real-Time Stock Prices** – Fetch live stock market data using `yfinance`.
* **Interactive Stock Charts** – Visualize stock trends over time.
* **Latest Financial News** – Get recent finance news headlines via Yahoo Finance RSS feeds.
* **Sentiment Analysis** – Analyze each headline’s sentiment as **Positive**, **Neutral**, or **Negative** using **FinBERT**.
* **Free & Open Source** – Build, run, and deploy without cost.

---

## 🧰 Tech Stack

| Layer             | Technology                                                 | Purpose                               |
| ----------------- | ---------------------------------------------------------- | ------------------------------------- |
| **Frontend**      | [Streamlit](https://streamlit.io/)                         | Interactive dashboard UI              |
| **Backend**       | Python                                                     | Core logic & AI integration           |
| **Stock Data**    | [yfinance](https://pypi.org/project/yfinance/)             | Fetch real-time stock prices          |
| **News Feed**     | [feedparser](https://pypi.org/project/feedparser/)         | Fetch financial news via RSS          |
| **AI Model**      | [FinBERT](https://huggingface.co/yiyanghkust/finbert-tone) | Sentiment analysis for financial news |
| **Visualization** | Streamlit Charts / Matplotlib                              | Display graphs and insights           |
| **Deployment**    | Streamlit Cloud / Hugging Face Spaces                      | Free hosting and deployment           |

---

## 📦 Project Structure

```
TrendTracker-AI/
├── app.py                 # Main Streamlit app
├── requirements.txt       # Python dependencies
├── utils/
│   ├── data_fetcher.py    # Functions to fetch stock data & news
│   └── sentiment.py       # Functions to perform FinBERT sentiment analysis
├── assets/
│   └── logo.png           # Optional images or icons
├── README.md              # Project documentation
└── .gitignore             # Git ignore file
```

---

## 💻 Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/TrendTracker-AI.git
cd TrendTracker-AI
```

2. **Create a virtual environment (optional but recommended)**

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the app**

```bash
streamlit run app.py
```

---

## 🧠 How It Works

1. **Fetch Stock Data:** Uses `yfinance` to get current stock prices and historical data.
2. **Fetch News Headlines:** Uses `feedparser` to pull financial news RSS feeds.
3. **Sentiment Analysis:** Headlines are analyzed using **FinBERT** to classify sentiment.
4. **Display Insights:** Shows interactive charts and sentiment summaries in the Streamlit dashboard.

---

## 🎨 Screenshots

<img width="1470" height="923" alt="Screenshot 2025-10-26 at 15 04 07" src="https://github.com/user-attachments/assets/fa31caa9-b1cc-4c24-bbd5-ccaa2dd9a0bb" />

<img width="348" height="750" alt="Screenshot 2025-10-26 at 15 07 23" src="https://github.com/user-attachments/assets/2ef0f669-26cb-4c48-a514-548112a2bbe0" />


---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## 🔗 References

* [yfinance Documentation](https://pypi.org/project/yfinance/)
* [feedparser Documentation](https://pypi.org/project/feedparser/)
* [FinBERT Model on Hugging Face](https://huggingface.co/yiyanghkust/finbert-tone)
* [Streamlit Documentation](https://docs.streamlit.io/)


