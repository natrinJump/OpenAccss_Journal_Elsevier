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
