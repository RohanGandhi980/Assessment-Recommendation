import re

def clean_text(text):
    """
    Lowercases, removes special characters, and extra spaces.
    """
    text = str(text).lower()
    text = re.sub(r'[^a-z0-9 ]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text
