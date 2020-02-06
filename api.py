import re
import cloudpickle

fh = open('data/ml_model.pkl', 'rb')
model = cloudpickle.loads(fh.read())

def run_search(q, n=10):
	probs = model.predict_proba([q])[0]
	lbld = list(zip(model.classes_, probs))
	lbld.sort(key=lambda x: x[1], reverse=True)
	strains = [x[0] for x in lbld]
	return strains[:n]