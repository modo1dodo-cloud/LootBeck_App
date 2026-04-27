from flask import Flask, request, jsonify
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "LootBeck Server is LIVE! To search, use: /search?name=Elon"

@app.route('/search')
def search():
    name_query = request.args.get('name', '')
    if not name_query:
        return jsonify({"found": False, "message": "اكتب اسماً للبحث عن الكنوز!"})
    
    try:
        # التأكد من وجود ملف البيانات
        if not os.path.exists('data.csv'):
            return jsonify({"found": False, "error": "ملف البيانات data.csv غير موجود"})
            
        df = pd.read_csv('data.csv')
        # كود البحث الذكي عن الأسماء
        results = df[df['name'].str.contains(name_query, case=False, na=False)]
        
        return jsonify({
            "found": True, 
            "count": len(results),
            "results": results.to_dict(orient='records')
        })
    except Exception as e:
        return jsonify({"found": False, "error": str(e)})

# السطر الذهبي لمنصة Vercel
app = app
