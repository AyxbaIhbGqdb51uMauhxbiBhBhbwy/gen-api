from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/test', methods=['GET'])
def test_api():
    return jsonify({"status": "success", "message": "API is working"}), 200
