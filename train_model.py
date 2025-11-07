from sklearn.feature_extraction.text import TfidfVectorizer
from text_cleaner import clean_text

def train_model(train_df):
    train_df["clean_query"] = train_df["Query"].apply(clean_text)
    vectorizer = TfidfVectorizer()
    train_vectors = vectorizer.fit_transform(train_df["clean_query"])
    print("TFIDF model trained on training queries.")
    return vectorizer, train_vectors
