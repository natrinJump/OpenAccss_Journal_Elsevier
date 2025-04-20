from transformers import AutoModel, AutoTokenizer
import numpy as np
from model_helper import *
import torch

class Model:
    def __init__(self):
        self.sciBert_model = AutoModel.from_pretrained("allenai/scibert_scivocab_uncased")
        self.tokenizer = AutoTokenizer.from_pretrained("allenai/scibert_scivocab_uncased")
        self.subj_acc, self.abstract_acc = load_model_accuracy()
        self.encoder = load_encoder()
        self.subject_vectorizer, self.subject_model = load_subject_model()
        self.abstract_model = load_abstract_models()
        self.journal_name_dict = load_journal_abv_dict()

    def get_embeddings(self, sentences, batch_size=50, max_length=500):
        with torch.no_grad():
            embeddings = []  # Initialize a list to accumulate embeddings
            for idx in range(0, len(sentences), batch_size):
                batched_sentences = sentences[idx : min(len(sentences), idx + batch_size)]
                encoded = self.tokenizer(batched_sentences, truncation=True, return_tensors='pt', padding="max_length", max_length=max_length)
                batch_embeddings = self.sciBert_model(**encoded).last_hidden_state[:, 0].cpu().numpy()
                embeddings.extend(batch_embeddings)  # Accumulate embeddings
            return np.array(embeddings)
        

    def abstract_predict(self, subj, abstract):
        model = self.abstract_model[subj]
        embedded_abstract = list(self.get_embeddings([abstract]))
        return model.predict(np.array(embedded_abstract))[0]


    def ranking(self, abstract, subjectarea):
        result = {
            'model_weights': {},
            'abstract_prediction': {

            },
            # 'subject_prediction',
            # 'final_prediction',
        }
        subjectarea = to_lower(subjectarea)

        subj_pred = self.subject_predict(subjectarea)

        total_accuracy = self.subj_acc
        for subject in subjectarea:
            total_accuracy += self.abstract_acc[subject]
        
        result['subject_prediction'] = self.prediction_formatter(subj_pred)
        subjarea_weight = self.subj_acc/total_accuracy
        result['model_weights']['subj_area_model'] = subjarea_weight
        
        abstract = clean_text(to_lower_str(abstract))

        total_abstract_pred = subj_pred * subjarea_weight
        for subject in subjectarea:
            pred = self.abstract_predict(subject, abstract)
            weight = self.abstract_acc[subject]/total_accuracy
            result['model_weights'][subject] = weight
            total_abstract_pred += pred * (weight)
            result['abstract_prediction'][subject] = self.prediction_formatter(pred)

        result['final_prediction'] = self.prediction_formatter(total_abstract_pred)
        return result
    

    def prepared_subject(self, subjectarea):
        subjectarea = to_lower(subjectarea)
        subjectarea = ' '.join(subjectarea)
        return self.subject_vectorizer.transform([subjectarea]).toarray()

    def subject_predict(self, subjectarea):
        subjectarea = self.prepared_subject(subjectarea)
        prediction = self.subject_model.predict(subjectarea)
        return prediction[0]
    
    def prediction_formatter(self, pred):
        pred_indexs = pred.argsort()[::-1]
        journal_class = self.encoder.classes_
        return [(self.journal_name_dict[journal_class[pred_index]], journal_class[pred_index], pred[pred_index]) for pred_index in pred_indexs]

