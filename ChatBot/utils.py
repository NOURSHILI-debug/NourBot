import re
def preprocess_text(text):
    """Preprocess the input text by converting to lowercase and removing special characters."""
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text.strip()