from flask import Flask, request, jsonify
from api import run_search

app = Flask(__name__)

@app.route('/')
def searching():
  q = request.args.get('q')
  return jsonify(run_search(q))