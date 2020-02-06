import re
import cloudpickle

fh = open('data/ml_model.pkl', 'rb')
model = cloudpickle.loads(fh.read())

def run_search(q):
	probs = model.predict_proba([q])[0]
	lbld = list(zip(model.classes_, probs))
	lbld.sort(key=lambda x: x[1], reverse=True)
	strains = [x[0] for x in lbld]
	return strains[:10]

if __name__ == '__main__':
	print(run_search('indica giggly happy'))
	print(run_search('frowny mean stupid'))