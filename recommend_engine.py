from sklearn.metrics.pairwise import cosine_similarity
from text_cleaner import clean_text

def recommend_assessment(test_query, vectorizer, train_vectors, train_df, top_k=3):
    """
    Returns top-k most similar assessment URLs for a given test query.
    """
    query_vec = vectorizer.transform([clean_text(test_query)])
    similarities = cosine_similarity(query_vec, train_vectors).flatten()

    # Rank the training queries by similarity
    ranked_indices = similarities.argsort()[::-1][:top_k]
    results = []
    for idx in ranked_indices:
        results.append({
            "Query": test_query,
            "Recommended_Assessment": train_df.iloc[idx]["Assessment_url"],
            "Similarity_Score": round(float(similarities[idx]), 3)
        })
    return results
