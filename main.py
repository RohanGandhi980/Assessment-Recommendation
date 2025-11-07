from data_loader import load_data
from train_model import train_model
from recommend_engine import recommend_assessment
import pandas as pd

if __name__ == "__main__":
    train_df, test_df = load_data("Gen_AI Dataset.xlsx")
    vectorizer, train_vectors = train_model(train_df)
    all_results = []
    for q in test_df["Query"]:
        top_results = recommend_assessment(q, vectorizer, train_vectors, train_df, top_k=3)
        all_results.extend(top_results)
    output_df = pd.DataFrame(all_results)
    with pd.ExcelWriter("Recommendations_Output.xlsx") as writer:
        output_df.to_excel(writer, sheet_name="Recommendations", index=False)
        summary = pd.DataFrame({
            "Metric": ["Total Queries", "Avg Similarity", "Top Match Confidence"],
            "Value": [len(test_df), round(output_df["Similarity_Score"].mean(), 3), round(output_df["Similarity_Score"].max(), 3)]
        })
        summary.to_excel(writer, sheet_name="Summary", index=False)
    print("Recommendations saved to Recommendations_Output.xlsx")
    print(output_df.head())
