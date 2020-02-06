import re
import cloudpickle
from spacy.lang.en import English
from spacy.lang.en.stop_words import STOP_WORDS
import os

nlp = English()
mystops = STOP_WORDS.union({
  'strain', 'strains', 'effect', 'effects', 'flavor', 'flavors',
  'bud', 'buds', ' ', '  ', '$', 'user', 'users', 'produce', 'produces',
  'showing', 'start', 'started', 'price', 'refers', 'packs', 'tends',
  'stem', 'stems', 'report', 'supposedly', 'breed', 'bred', 'seed', 'seeds',
  'intermittent', 'week', 'combine', 'combines', 'containing', '\xa0',
  'smell', 'give', 'gives', 'explanation', 'call', 'calls', 'match', 'matches',
  'making', 'tend', 'lineage', 'probably', 'especially', 'utilizing', 'offer',
  'offers', 'technique', 'techniques', 'like', 'including'
})

def token_str(s):
  if (type(s)) != str:
    return list()
  
  s = s.lower()
  s = re.sub(r'[\.,!?\\\-\$_]', ' ', s)
  s = re.sub(r' +', ' ', s)
  s = s.strip()
  
  if s == 'None' or s == '':
    return list()
  return [
    t.lemma_ for t in nlp(s)
    if t.lemma_ not in mystops and not t.is_punct
  ]

fn = os.path.join(os.path.dirname(__file__), '../data/token_str.pkl')
pkl = cloudpickle.dumps(token_str)
with open(fn, 'wb') as fh:
  fh.write(pkl)