import os
import pandas as pd
from langchain_core.documents import Document
from langchain_community.retrievers import BM25Retriever
from langchain.retrievers import EnsembleRetriever
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv() 

# Gemini API Studio key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

# Load your CSV
df = pd.read_csv("financial_data.csv")

# Convert to docs
documents = []
for _, row in df.iterrows():
    content = f"""
    Date: {row['Date']}
    Description: {row['Description']}
    Category: {row['Category']}
    Amount: {row['Amount']}
    Type: {row['Type']}
    """
    documents.append(Document(page_content=content))

# TF-IDF for dense
texts = [doc.page_content for doc in documents]
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(texts)

def dense_retriever(query, top_k=5):
    query_vec = tfidf.transform([query])
    sims = cosine_similarity(query_vec, tfidf_matrix).flatten()
    ranked = sims.argsort()[::-1][:top_k]
    return [documents[i] for i in ranked]

# BM25
sparse_retriever = BM25Retriever.from_documents(documents)

def hybrid_retriever(query):
    dense_docs = dense_retriever(query, top_k=5)
    sparse_docs = sparse_retriever.get_relevant_documents(query)
    # deduplicate
    all_docs = {doc.page_content: doc for doc in dense_docs + sparse_docs}
    return list(all_docs.values())

# Gemini direct (AI Studio)
model = genai.GenerativeModel("gemini-2.0-flash")

def answer_query(query):
    relevant_docs = hybrid_retriever(query)
    context = "\n".join(doc.page_content for doc in relevant_docs)
    prompt = f"""
Answer the following question based on these documents:

{context}

Question: {query}
"""
    response = model.generate_content(prompt)
    return response.text
