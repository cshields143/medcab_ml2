import re
import cloudpickle

fh = open('data/word_vect.pkl', 'rb')
word_vect = cloudpickle.loads(fh.read())

fh = open('data/ml_model.pkl', 'rb')
model = cloudpickle.loads(fh.read())

if __name__ == '__main__':
	egq = 'indica giggly happy'
	in_vec = word_vect.transform([egq])
	probs = model.predict_proba(in_vec)
	print(probs)