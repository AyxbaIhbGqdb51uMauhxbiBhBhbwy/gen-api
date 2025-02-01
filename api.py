from flask import Flask, jsonify, request
import random

app = Flask(__name__)

# Daftar API key yang valid
VALID_API_KEYS = {
    "nsnseuhusdjcneusbbeuuisefb-OWNERONLY": "never off",
    "oCz5ODELLOIzD3dgbIMnoy3-jova3435": "never off"
}

def get_random_account(filename):
    try:
        with open(filename, 'r') as file:
            accounts = file.readlines()
        if not accounts:
            return {"error": "No accounts found"}
        random_account = random.choice(accounts).strip()
        if ":" in random_account:
            username, password = random_account.split(":", 1)
            return {
                "combo": f"{username}:{password}",
                "username": username,
                "password": password,
                "Service": "Roblox, Steam, Valorant, NordVpn, Netflix, Disney+, Crunchyroll."
            }
        else:
            return {"error": "Invalid account format"}
    except Exception as e:
        return {"error": str(e)}

@app.route('/api/<service>', methods=['GET'])
def random_account(service):
    # Ambil API key dari query parameter atau header
    api_key = request.args.get("apikey") or request.headers.get("x-api-key")

    if not api_key or api_key not in VALID_API_KEYS:
        return jsonify({"error": "Invalid API key"})

    # Peta layanan ke nama file
    file_map = {
        "Roblox": "accrblx.txt",
        "Steam": "accsteam.txt",
        "Crunchyroll": "acccrunchyroll.txt",
        "Netflix": "accnetflix.txt",
        "Valorant": "accvalorant.txt",
        "NordVpn": "accnordvpn.txt",
        "Fortnite": "accfortnite.txt",
        "Disney": "accdisneyplus.txt"
    }

    # Cek apakah layanan tersedia
    if service not in file_map:
        return jsonify({"error": "Service not found"})

    return jsonify(get_random_account(file_map[service]))

if __name__ == '__main__':
    app.run(debug=True)
