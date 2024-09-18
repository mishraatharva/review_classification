import os
import pickle
from constants import *

# def load_model():
#     model_path = os.path.join(MODEL_PATH, MODEL_NAME)
#     with open(model_path, "rb") as file:
#         model = pickle.load(file)
#     return model

def load_model():
    model_path = os.path.join(MODEL_PATH, MODEL_NAME)
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model