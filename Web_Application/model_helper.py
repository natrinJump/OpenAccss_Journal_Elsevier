import pickle
import os
from keras.models import load_model
import re

def load_encoder():
    le_filename = 'data/labelencoder.pkl'
    # load the model from disk
    with open(le_filename, 'rb') as f:
        le = pickle.load(f)
        return le
    exit(-1)


def load_subject_model():
    """
    Load subject model including vectorizer

    :param parameter1: Vectorizer
    :param parameter2: Subject model
    """
    subject_model = load_model('data/subjModel/subjArea.h5')
        
    subject_vect_filename = 'data/subjModel/subj_vectorizer.pkl'
    # load the model from disk
    with open(subject_vect_filename, 'rb') as f:
        subj_vectorizer = pickle.load(f)

    return subj_vectorizer, subject_model

def load_abstract_models():
    abstract_model = {}

    directory_path = 'data/abstractModel/'

    file_list = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

    for file in file_list:
        abstract_model[file[:4].lower()] = load_model(directory_path + file)

    return abstract_model


def to_lower(X):
    X = [x.lower() for x in X]
    return X

def load_journal_abv_dict():
    file_path = 'data/journal_abv_dictionary.pkl'
    with open(file_path, 'rb') as f:
        return pickle.load(f)


def load_model_accuracy():
    file_path = 'data/model_accuracy.pkl'
    with open(file_path, 'rb') as f:
        return pickle.load(f)
    
def clean_text(X):
    X = re.sub('[^a-z\s]+', '', X)
    return X

def to_lower_str(X):
    X = X.lower()
    return X