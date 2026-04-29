from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return "LootBeck Engine is Live! To search, use /search?name=Elon"

@app.route('/search')
def search():
    name_query = request.args.get('name', '')
    try:
        df = pd.read_csv('data.csv')
        results = df[df['name'].str.contains(name_query, case=False, na=False)]
        return jsonify(results.to_dict(orient='records'))
    except Exception as e:
        return jsonify({"error": str(e)})

# السطر الأهم لـ Vercel
app = app
