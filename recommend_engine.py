from sklearn.metrics.pairwise import cosine_similarity
from text_cleaner import clean_text

def recommend_assessment(test_query, vectorizer, train_vectors, train_df, top_k=3):
    query_vec = vectorizer.transform([clean_text(test_query)])
    similarities = cosine_similarity(query_vec, train_vectors).flatten()
    ranked_indices = similarities.argsort()[::-1]
    results = []
    for idx in ranked_indices:
        if similarities[idx] < 0.25:
            continue
        train_query = train_df.iloc[idx]["Query"]
        overlap = set(clean_text(test_query).split()) & set(clean_text(train_query).split())
        if overlap:
            explanation = f"Recommended because the job description shares key focus areas such as {', '.join(overlap)}"
        else:
            explanation = "Recommended based on overall contextual similarity."
        url = train_df.iloc[idx]["Assessment_url"]
        name = url.split("/")[-2].replace("-", " ").title() if isinstance(url, str) and "/" in url else url
        results.append({
            "Query": test_query,
            "Recommended_Assessment_Name": name,
            "Recommended_Assessment": url,
            "Similarity_Score": round(float(similarities[idx]), 3),
            "Explanation": explanation
        })
        if len(results) >= top_k:
            break
    return results
