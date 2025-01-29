from flask import Flask, jsonify
import random

app = Flask(__name__)

def get_random_account(filename):
    try:
        # Membaca file
        with open(filename, 'r') as file:
            accounts = file.readlines()

        # Memastikan file tidak kosong
        if not accounts:
            return {"error": "No accounts found"}, 404

        # Memilih satu baris acak
        random_account = random.choice(accounts).strip()

        # Memisahkan username dan password
        if ":" in random_account:
            username, password = random_account.split(":", 1)
            return {
                "username": username,
                "password": password,
                "combo": random_account
            }, 200
        else:
            return {"error": "Invalid account format"}, 400
    except Exception as e:
        return {"error": str(e)}, 500

@app.route('/api/Roblox', methods=['GET'])
def random_roblox_account():
    return jsonify(*get_random_account('accrblx.txt'))

@app.route('/api/Steam', methods=['GET'])
def random_steam_account():
    return jsonify(*get_random_account('accsteam.txt'))

@app.route('/api/Crunchyroll', methods=['GET'])
def random_crunchyroll_account():
    return jsonify(*get_random_account('acccrunchyroll.txt'))

@app.route('/api/Netflix', methods=['GET'])
def random_netflix_account():
    return jsonify(*get_random_account('accnetflix.txt'))


@app.route('/api/Valorant', methods=['GET'])
def random_valorant_account():
    return jsonify(*get_random_account('accvalorant.txt'))


 

@app.route('/api/PornHub', methods=['GET'])
def random_cornhub_account():
    return jsonify(*get_random_account('acccornhub.txt'))

@app.route('/api/NordVpn', methods=['GET'])
def random_nordvpn_account():
    return jsonify(*get_random_account('accnordvpn.txt'))


@app.route('/api/Fortnite', methods=['GET'])
def random_fortnite_account():
    return jsonify(*get_random_account('accfortnite.txt'))

@app.route('/api/Disney', methods=['GET'])
def random_disneyplus_account():
    return jsonify(*get_random_account('accdisneyplus.txt'))

if __name__ == '__main__':
    app.run(debug=True)
