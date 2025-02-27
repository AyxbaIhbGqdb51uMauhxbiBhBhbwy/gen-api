from flask import Flask, jsonify, request
import random

app = Flask(__name__)

# Daftar API key yang valid
VALID_API_KEYS = {
    "nsnseuhusdjcneusbbeuuisefb-OWNERONLY": "never off",
    "oCz5ODELLOIzD3dgbIMnoy3-jova3435": "never off"
}

# Peta layanan ke nama file
FILE_MAP = {
    "Roblox": "accrblx.txt",
    "Steam": "accsteam.txt",
    "Crunchyroll": "acccrunchyroll.txt",
    "Netflix": "accnetflix.txt",
    "Valorant": "accvalorant.txt",
    "NordVpn": "accnordvpn.txt",
    "OnlyFans": "acconlyfans.txt",
    "Disney": "accdisneyplus.txt"
}

def get_random_accounts(filename, bulk=1):
    try:
        with open(filename, 'r') as file:
            accounts = [line.strip() for line in file.readlines() if ":" in line]
        if not accounts:
            return {"error": "No valid accounts found"}
        
        bulk = min(bulk, len(accounts))  # Pastikan tidak melebihi jumlah akun tersedia
        selected_accounts = random.sample(accounts, bulk)
        
        return [{"combo": acc, "username": acc.split(":", 1)[0], "password": acc.split(":", 1)[1]} for acc in selected_accounts]
    except Exception as e:
        return {"error": str(e)}

@app.route('/genaccount', methods=['GET'])
def generate_accounts():
    # Ambil API key dari query parameter atau header
    api_key = request.args.get("apikey") or request.headers.get("x-api-key")
    if not api_key or api_key not in VALID_API_KEYS:
        return jsonify({"error": "Invalid API key"}), 403
    
    # Ambil parameter layanan
    service = request.args.get("service")
    if service not in FILE_MAP:
        return jsonify({"error": "Service not found"}), 404
    
    # Ambil jumlah akun yang diminta (default 1)
    try:
        bulk = int(request.args.get("bulk", 1))
        if bulk < 1:
            raise ValueError
    except ValueError:
        return jsonify({"error": "Invalid bulk value"}), 400
    
    return jsonify(get_random_accounts(FILE_MAP[service], bulk))

if __name__ == '__main__':
    app.run(debug=True)
