from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/search')
def search():
    name = request.args.get('name', '')
    try:
        # قراءة مباشرة لملف البيانات
        df = pd.read_csv('data.csv')
        results = df[df['name'].str.contains(name, case=False, na=False)]
        return jsonify(results.to_dict(orient='records'))
    except Exception as e:
        return jsonify({"error": "Data not found", "details": str(e)})

@app.route('/')
def home():
    return "LootBeck is Live! Search now."

app = app
