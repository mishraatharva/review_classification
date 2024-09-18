from constants import *
from tensorflow.keras.preprocessing import sequence

def preprocess_text(text):
    words = text.lower().split()
    encoded_review = [WORD_INDEX.get(word, 2) + 3 for word in words]
    if len(encoded_review) < 500:
        padded_review = sequence.pad_sequences([encoded_review], maxlen=500)
    else:
        pass
    return padded_review