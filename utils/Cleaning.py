import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import words
import contractions
import re
from nltk.corpus import stopwords

nltk.download('words')
nltk.download('punkt')

def remove_non_chars(text):
    """
    Quitar lo que no sean letras
    """
    removed_chars = re.findall(r'[^a-zA-Z\s]', text)
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text)
    return cleaned_text 

def separate_words(text):
    """
    Utilizamos una expresión regular para encontrar transiciones de minúsculas a mayúsculas y separar las palabras
    """
    words_separated = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
    return words_separated

def lowercase_text(text):
    """
    Poner en miniscula
    """
    return text.lower()

def expand_contractions(text: str)-> str:
    """
    Expandir las contracciones
    """
    expanded_text = contractions.fix(text)
    return expanded_text

def remove_non_english_words(text):
    """
    Quitar palabras que no esten en ingles
    """
    english_vocab = set(words.words())
    words_in_text = nltk.word_tokenize(text)
    english_words = [word for word in words_in_text if word.lower() in english_vocab]
    cleaned_text = ' '.join(english_words)
    return cleaned_text

def remove_stopwords(text):
    """
    Quitar palabras vacías (stopwords)
    """
    tokens = nltk.word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
    cleaned_text = ' '.join(filtered_tokens)
    return cleaned_text

def clean_text(text):
    """
    Limpia el texto utilizando todas las funciones proporcionadas
    """
    text = remove_non_chars(text)
    text = separate_words(text)
    text = lowercase_text(text)
    text = expand_contractions(text)
    text = remove_non_english_words(text)
    text = remove_stopwords(text)
    return text


