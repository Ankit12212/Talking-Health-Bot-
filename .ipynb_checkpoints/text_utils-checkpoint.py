import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

def tokenize_and_lemma(text):
    tokens = nltk.word_tokenize(text.lower())
    return [lemmatizer.lemmatize(t) for t in tokens]