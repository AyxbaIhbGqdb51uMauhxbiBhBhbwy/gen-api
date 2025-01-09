from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/api/gen-rblx', methods=['GET'])
def random_account():
    try:
        # Membaca file acc.txt
        with open('acc.txt', 'r') as file:
            accounts = file.readlines()
        
        # Memastikan file tidak kosong
        if not accounts:
            return jsonify({"error": "No accounts found"}), 404
        
        # Memilih satu baris acak
        random_account = random.choice(accounts).strip()
        
        # Memisahkan username dan password
        if ":" in random_account:
            username, password = random_account.split(":", 1)
            return jsonify({
                           "username": username,
                "password": password,
                "combo": random_account
            }), 200
        else:
            return jsonify({"error": "Invalid account format"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
