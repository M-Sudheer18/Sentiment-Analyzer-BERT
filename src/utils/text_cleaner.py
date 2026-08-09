import re 
import html
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Safely download required NLTK data on first run
for dependency in ['stopwords', 'wordnet', 'punkt']:
    try:
        if dependency == "stopwords":
            nltk.data.find('corpora/stopwords')
        elif dependency == "wordnet":
            nltk.data.find('corpora/wordnet')
        else:
            nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download(dependency, quiet=True)

class TextCleaner:
    # Initialize these at the class level so they are loaded into memory only once
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()

    @classmethod
    def clean(cls, text: str) -> str:
        # Cleans input text
        if not isinstance(text, str):
            return ""
        if not text:
            return ""

        # Lowercase and Unescape HTML
        text = text.lower()
        text = html.unescape(text)

        # Remove URLs, Mentions, Hashtags, and Digits
        text = re.sub(r"http\S+|https\S+|www\S+", "", text)
        text = re.sub(r"@\w+", "", text)
        text = re.sub(r"#", "", text)
        text = re.sub(r"\d+", "", text)

        # Remove Punctuations
        text = text.translate(
            str.maketrans(
                "", "", string.punctuation
            )
        )

        # Remove Extra White Spaces
        text = re.sub(r"\s+", " ", text).strip()

        # Tokenize, Lemmatize, and Remove Stop Words
        tokens = word_tokenize(text)
        tokens = [
            cls.lemmatizer.lemmatize(word)
            for word in tokens
            if word not in cls.stop_words
        ]
        return " ".join(tokens) 