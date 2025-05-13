
import requests

# Token Mint
TOKEN_MINT = "U4LQFLQKAziV92BGrH33wyVmGhicJhsfjxUdU3CcGFM"

# Step Finance API endpoint (unofficial public access)
def fetch_holders():
    url = f"https://api.step.finance/v1/tokenholders?token={TOKEN_MINT}&limit=1000"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            holders = [entry["holder"] for entry in data]
            print(f"{len(holders)} Wallets gefunden.")
            for w in holders:
                print(w)
            return holders
        else:
            print("Fehler bei Step API:", response.status_code, response.text)
            return []
    except Exception as e:
        print("Fehler beim Abruf:", str(e))
        return []

if __name__ == "__main__":
    fetch_holders()
