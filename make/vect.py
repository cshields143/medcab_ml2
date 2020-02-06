import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import cloudpickle
import os

this_path = os.path.dirname(__file__)
fn_old = os.path.join(this_path, '../data/fulltext.csv')
fn_new = os.path.join(this_path, '../data/word_vect.pkl')
fn_tok = os.path.join(this_path, '../data/token_str.pkl')

fh = open(fn_tok, 'rb')
token_str = cloudpickle.loads(fh.read())
df = pd.read_csv(fn_old)

def dummy(x): return x
vect = TfidfVectorizer(
	preprocessor=dummy,
	tokenizer=token_str,
	analyzer='word'
)
vect.fit(df['fulltext'])

with open(fn_new, 'wb') as fh:
	fh.write(cloudpickle.dumps(vect))