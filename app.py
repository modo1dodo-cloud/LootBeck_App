from flask import Flask, request, jsonify
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "LootBeck Server is LIVE!"

@app.route('/search', methods=['GET'])
def search():
    name_query = request.args.get('name', '')
    try:
        # التأكد من وجود ملف البيانات
        if not os.path.exists('data.csv'):
            return jsonify({"found": False, "error": "data.csv missing"})
            
        df = pd.read_csv('data.csv')
        results = df[df['name'].str.contains(name_query, case=False, na=False)]
        return jsonify({"found": True, "results": results.to_dict(orient='records')})
    except Exception as e:
        return jsonify({"found": False, "error": str(e)})

# هذا السطر هو الأهم لعمل Vercel
app = app
