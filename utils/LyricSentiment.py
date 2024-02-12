from transformers import pipeline

import nltk
from nltk.corpus import words, stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

from functools import reduce

model = "SamLowe/roberta-base-go_emotions"
classifier = pipeline(task="text-classification", model=model, top_k=None)

nltk.download('words')
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

def __analyze(lyrics: str) -> dict:
    try:
        sentiments = classifier(lyrics)[0]
    except (Exception):
        print(f'Error with lyrics: {lyrics}')
        return {}
    sentiments = map(lambda dict: {dict.get('label').capitalize(): dict.get('score')}, sentiments)
    sentiments = reduce(lambda x, y: x | y, sentiments, {})
    return sentiments

def __clear(lyrics: str) -> str:
    lyrics = lyrics.lower()

    tokens = word_tokenize(lyrics)

    english_words = set(words.words())
    tokens = [token for token in tokens if token in english_words]

    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]

    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]

    lyrics = ' '.join(tokens)
    return lyrics

def sentiments(lyrics: str) -> dict:
    lyrics = __clear(lyrics)
    if len(lyrics) == 0: return {}
    else: return __analyze(lyrics)

def set_model(new_model: str):
    model = new_model
    classifier = pipeline(task="text-classification", model=model, top_k=None)
