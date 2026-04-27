import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "LootBack Engine is Live! To search, add /search?name=YourName to the URL"

@app.route('/search', methods=['GET'])
def search():
    name_query = request.args.get('name', '')
    if not name_query:
        return jsonify({"found": False, "message": "Please enter a name to search"})
    
    try:
        df = pd.read_csv('data.csv')
        # بحث مرن يجد الأسماء حتى لو كانت جزءاً من النص
        results = df[df['name'].str.contains(name_query, case=False, na=False)]
        return jsonify({"found": True, "results": results.to_dict(orient='records')})
    except Exception as e:
        return jsonify({"found": False, "message": "Database error", "error": str(e)})

# مهم جداً لـ Vercel
app = app
