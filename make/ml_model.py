import pandas as pd
import cloudpickle
import os
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

this_path = os.path.dirname(__file__)
fn_dat = os.path.join(this_path, '../data/fulltext.csv')
fn_vec = os.path.join(this_path, '../data/word_vect.pkl')
fn_mod = os.path.join(this_path, '../data/ml_model.pkl')

fh = open(fn_vec, 'rb')
vec = cloudpickle.loads(fh.read())
df = pd.read_csv(fn_dat)

clf = LogisticRegression()
pipe = Pipeline([
  ('vec', vec),
  ('clf', clf)
])
pipe.fit(df['fulltext'], df['Strain'])

with open(fn_mod, 'wb') as fh:
  fh.write(cloudpickle.dumps(pipe))