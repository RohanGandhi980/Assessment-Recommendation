import streamlit as st
import pandas as pd
from data_loader import load_data
from train_model import train_model
from recommend_engine import recommend_assessment

st.set_page_config(page_title="SHL Assessment Recommender", layout="centered")
st.title("SHL Assessment Recommendation (TF–IDF)")

train_df, _ = load_data("Gen_AI Dataset.xlsx")
vectorizer, train_vectors = train_model(train_df)

query = st.text_area("Enter a job description or hiring query:", height=160)
k = st.slider("Top-K Results", 1, 5, 3)
run = st.button("Recommend")

if run and query.strip():
    results = recommend_assessment(query, vectorizer, train_vectors, train_df, top_k=k)
    if results:
        st.success("Recommendations")
        st.dataframe(pd.DataFrame(results))
    else:
        st.warning("No high-confidence match found.")
