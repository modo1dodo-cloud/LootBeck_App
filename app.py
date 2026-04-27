import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    name_query = request.args.get('name', '')
    try:
        df = pd.read_csv('data.csv')
        results = df[df['name'].str.contains(name_query, case=False, na=False)]
        return jsonify({"found": True, "results": results.to_dict(orient='records')})
    except:
        return jsonify({"found": False, "message": "Database error"})

if __name__ == "__main__":
    app.run()
