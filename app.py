from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/search')
def search():
    name_query = request.args.get('name', '')
    try:
        df = pd.read_csv('data.csv')
        # بحث مرن عن الاسم
        results = df[df['name'].str.contains(name_query, case=False, na=False)]
        return jsonify(results.to_dict(orient='records'))
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/')
def home():
    return "LootBeck is Live! Search now."

app = app
