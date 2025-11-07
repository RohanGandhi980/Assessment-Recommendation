from sklearn.metrics.pairwise import cosine_similarity
from text_cleaner import clean_text

def recommend_assessment(test_query, vectorizer, train_vectors, train_df, top_k=3):
    query_vec = vectorizer.transform([clean_text(test_query)])
    similarities = cosine_similarity(query_vec, train_vectors).flatten()

    # Ranking the training queries by similarity
    ranked_indices = similarities.argsort()[::-1][:top_k]

    results = []
    for idx in ranked_indices:
        train_query = train_df.iloc[idx]["Query"]

        overlap = set(clean_text(test_query).split()) & set(clean_text(train_query).split())
        if overlap:
            explanation = f"Matched due to overlap in key terms: {', '.join(overlap)}"
        else:
            explanation = "Matched based on overall semantic similarity."

        results.append({
            "Query": test_query,
            "Recommended_Assessment": train_df.iloc[idx]["Assessment_url"],
            "Similarity_Score": round(float(similarities[idx]), 3),
            "Explanation": explanation
        })

    return results
