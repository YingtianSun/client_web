from flask import Flask, request, jsonify
from extractor.fetch import extract_company_info

app = Flask(__name__)

@app.route("/extract_company_info", methods=["POST"])
def extract_info():
    url = request.json.get("url")
    if not url:
        return jsonify({"error": "Missing 'url' in JSON."}), 400

    result = extract_company_info(url)
    return jsonify(result)

if __name__ == "__main__":
    app.run(port=5055, debug=True)