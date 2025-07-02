# 💰 AI Accounting RAG Assistant

This project is a proof-of-concept personalized accounting assistant built with a **hybrid Retrieval-Augmented Generation (RAG)** pipeline. It answers natural language questions about a user’s financial transactions, combining dense (TF-IDF) and sparse (BM25) retrieval with a Gemini large language model for fluent, human-like responses.

---

## 🚀 Features

✅ Answers questions about your own financial data
✅ Uses a hybrid retrieval (TF-IDF + BM25) for robust search
✅ Generates flexible, natural responses using Gemini
✅ Simple Gradio chat interface
✅ Easy to extend for production

---

## 📁 Project Structure

```bash
.
├── rag_hybrid.py
├── rag_ui_hybrid.py
├── financial_data.csv
├── image1.png
├── .env
└── requirements.txt
```

---

## 🛠️ Installation

First, clone this repository:

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

Then create a Python environment:

```bash
conda create -n rag-assistant python=3.10
conda activate rag-assistant
```

and install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 API Key Setup (.env)

The system uses Gemini (Google AI Studio) to generate responses. You will need to:

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Generate an API key
3. Create a file named `.env` in the project root with this content:

```env
GOOGLE_API_KEY=your_actual_api_key_here
```

**Important:** never commit your `.env` file to a public repository!

The project loads this automatically using `python-dotenv`.

---

## ▶️ Running the Assistant

Simply start the Gradio chat:

```bash
python rag_ui_hybrid.py
```

This will open a local server (usually on `http://127.0.0.1:7860`) with a friendly chat interface.

---

## 💬 Example Questions

* *"How much did I spend on software subscriptions last month?"*
* *"What were my biggest expenses?"*
* *"Did I have any revenue from Project X?"*
* *"Summarize my travel expenses."*

---

## 📄 How It Works

✅ The hybrid retriever indexes your CSV transaction data:

* **Dense semantic** search via TF-IDF
* **Sparse** keyword search via BM25

✅ When you ask a question, it retrieves the top relevant rows from both, merges them, and sends them as context to Gemini (LLM) for a natural-language answer.

This combines **accuracy** (from keyword) and **flexibility** (from semantic) in one system.

---

## 🌟 Why Hybrid RAG?

* Traditional dashboards can only show fixed charts
* RAG allows open-ended, natural conversation
* Hybrid (dense + sparse) gives the best coverage for your small tabular data

---

## 📷 Screenshot

Replace `image1.png` with your working Gradio screenshot if you like!

---

## 📝 Credits

* Built with [LangChain](https://www.langchain.com/)
* [scikit-learn](https://scikit-learn.org/)
* [Gradio](https://gradio.app/)
* [Gemini](https://makersuite.google.com/app)

---

Happy Accounting 🚀
