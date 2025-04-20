# Open terminal and do: py -3 -m venv .venv
# Then: .venv\Scripts\activate
# Then run: pip install -r requirements.txt
# Lastly: flask --app app.py run
# Or for debeg mode: flask --app app.py run --debug

from flask import Flask, render_template, request, flash, url_for, redirect
from journal_model import Model

app = Flask(__name__)
app.config['SECRET_KEY'] = 'very_secret_key_here'
model = Model()
rank_from = 5

@app.route('/')
def hello():
  return render_template('base.html')

@app.route('/run', methods=('GET', 'POST'))
def run():
  if request.method == 'POST':
    abstract = request.form['abstract']
    subj_areas = request.form.getlist('subj-area')

    if not abstract:
      flash('Abstract is required!')

    if not subj_areas:
      flash('At least one subject area is required!')
    
    journals = model.ranking(abstract, subj_areas)

  return render_template('result.html', journals=journals)


# def getJournals(abstract, subj_areas):
#   return model.ranking(abstract, subj_areas)[:rank_from]