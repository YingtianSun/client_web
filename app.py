from flask import Flask, request, jsonify
from extractor.fetch import extract_company_info
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy", "message": "Company info extractor is running"})

@app.route("/extract_company_info", methods=["POST"])
def extract_info():
    url = request.json.get("url")
    if not url:
        return jsonify({"error": "Missing 'url' in JSON."}), 400

    result = extract_company_info(url)
    return jsonify(result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5055))
    app.run(host="0.0.0.0", port=port, debug=False)
