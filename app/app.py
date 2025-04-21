import streamlit as st
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

st.title("🧠 Search Neuroscience Papers")
st.write("Enter a topic like 'mitral cells in learning'")

df = pd.read_csv("data/paragraph_data.csv")
embeddings = np.load("data/paragraph_embeddings.npy")
model = SentenceTransformer("all-MiniLM-L6-v2")

query = st.text_input("Search Query:")

if query:
    query_emb = model.encode([query])
    scores = cosine_similarity(query_emb, embeddings)[0]
    top_indices = scores.argsort()[-5:][::-1]

    for idx in top_indices:
        st.markdown(f"**{df.iloc[idx]['source']}**")
        st.write(df.iloc[idx]['text'])
        st.markdown("---")
