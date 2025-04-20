# Source Code

By: Tintin Wongthanaporn, Thijs Beumer, Jason Hsu & Jump Srinualnad

## Explanation of Each File and Folder

- The Open Access Project file is where we prepared our data and trained the models.
- The Scrape journal name file is where we managed to find the entire names of the journals (since journal names are abbreviated within the dataset).
- The Test predictor file is where we evaluated the models and tested different weights for each model to achieve the final prediction.
- The 'data' folder includes:
  - open_access_journal: A CSV file that contains the dataset after transformation from the original JSON files, application of listwise deletion, and removal of unimportant features.
  - body_extracted: A CSV file that structures the body text into a correct format from the open_access_journal.
- The 'models' folder: All trained models, including both abstract models and the subject area model, are stored here. Additionally, the folder includes pickle files, such as embeddings, vectorizer, and label encoder, to expedite code execution.
- The 'Journal Finder Web Application' folder: Inside this folder, you can find another README file. It will guide you on how to run our Journal Finder web application.

## Important Notes

- In our source code, there are certain sections that take an super long period to run, such as the training of abstract models in the **Open Access Project** file, which totals approximately 15 hours for generating embeddings and training models. Fortunately, we have preserved all the embeddings as pickle files. Consequently, you can bypass the step involving the generation of embeddings and proceed directly to the 'Load embeddings' section. The remaining portion, which involves training the models, is expected to take approximately 30 minutes. We have retained the code used to generate the embeddings in the file, so if needed, it is available for reference.
- We have commented out the codes used to save models and other elements to prevent redundant creation.
- When running the codes (excluding the web application), please ensure that the file paths are correct before execution. All required elements are located in the 'data' and 'models' folders. Please note that there is a 'data' folder within the 'Journal Finder Web Application' directory, exclusively used by the web application and distinct from the 'data' folder located externally.
- If you encounter any issues, whether with running the codes or the web application, please reach out to us via our student emails.

# 📚 Journal Finder: NLP for Academic Publishing

This project explores how **Natural Language Processing (NLP)** can assist researchers in selecting the most suitable academic journal for their publications. Built by a team of Technical Computer Science students at the University of Twente, our tool helps reduce the time and complexity involved in the journal selection process.

## 🚀 What We Built

We created a **Journal Finder** web application powered by a combination of deep learning models. Given a paper’s abstract and subject area(s), our system recommends the **top 5 most relevant journals** for submission.

### Key Highlights:
- Trained on **35,370** open-access articles from the Elsevier OA CC-BY dataset.
- Developed **26 subject-specific abstract models** using SciBERT embeddings.
- Built an additional **subject area model** using a bag-of-words approach.
- Combined predictions using a **dynamic accuracy-based weighting system**.

## 🧠 How It Works

1. **Data Preparation**
   - Cleaned and filtered article metadata and full texts.
   - Extracted and formatted features such as abstracts, subject areas, and DOIs.

2. **Model Training**
   - **Abstract models** (one per subject area) trained with SciBERT + a simple neural network classifier.
   - **Subject area model** trained using softmax regression on bag-of-words vectors.

3. **Prediction Fusion**
   - Combined outputs using dynamic model weighting based on test accuracies.
   - Final recommendation list shows the top 5 journals with confidence scores.

4. **Web Application**
   - Users input their abstract and subject areas.
   - App displays best-matching journals with explanations and visualization of model influences.

## 📊 Results

| Metric                  | Value       |
|------------------------|-------------|
| Top-1 Accuracy          | 76.8%       |
| Top-3 Accuracy          | 93.4%       |
| **Top-5 Accuracy**      | **96.9%**   |

Our model significantly outperforms random guessing (0.26% accuracy), making it a powerful tool to aid authors in journal selection.

---

> Built with by Jason Hsu, Jump Srinualnad, Tintin Wongthanaporn, and Thijs Beumer  
> Supervised by N. Bouali | University of Twente | 2023
