
import requests
import time
import json
from collections import defaultdict

API_KEY = "aa509418-fb9a-4d01-80b4-f603220b5148"
TOKEN_ADDRESS = "361HPgXyGNvuvVBNKQuUwRtbBbaDeMwdoRAGL1s7jay4"
OUTPUT_FILE = "leaderboard.json"

def fetch_token_activity():
    url = f"https://api.helius.xyz/v0/token-transfers?api-key={API_KEY}"
    response = requests.post(url, json={
        "mint": TOKEN_ADDRESS,
        "limit": 1000,
        "direction": "both"
    })
    if response.status_code != 200:
        print("Fehler beim Abrufen:", response.text)
        return []
    return response.json().get("transfers", [])

def build_leaderboard(transfers):
    leaderboard = defaultdict(float)
    for tx in transfers:
        if not tx.get("amount", 0): continue
        from_wallet = tx.get("fromUserAccount")
        to_wallet = tx.get("toUserAccount")
        sol_price = tx.get("nativeAmount", {}).get("amount", 0) / 1e9
        volume = abs(sol_price)

        if from_wallet: leaderboard[from_wallet] += volume
        if to_wallet: leaderboard[to_wallet] += volume
    sorted_lb = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
    return [{"wallet": k, "volume_in_SOL": round(v, 3)} for k, v in sorted_lb]

def save_to_file(data):
    with open(OUTPUT_FILE, "w") as f:
        json.dump(data, f, indent=2)

def main_loop():
    while True:
        try:
            transfers = fetch_token_activity()
            leaderboard = build_leaderboard(transfers)
            save_to_file(leaderboard)
            print("Leaderboard aktualisiert.")
        except Exception as e:
            print("Fehler:", e)
        time.sleep(60)

if __name__ == "__main__":
    main_loop()
