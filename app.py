import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "LootBeck Server is LIVE!"

@app.route('/search', methods=['GET'])
def search():
    name_query = request.args.get('name', '')
    try:
        df = pd.read_csv('data.csv')
        results = df[df['name'].str.contains(name_query, case=False, na=False)]
        return jsonify({"found": True, "results": results.to_dict(orient='records')})
    except Exception as e:
        return jsonify({"found": False, "error": str(e)})

app = app
