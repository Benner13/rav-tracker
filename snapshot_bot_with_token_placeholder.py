
import requests
import csv
import os
import subprocess

# CONFIGURATION
TOKEN_MINT = "U4LQFLQKAziV92BGrH33wyVmGhicJhsfjxUdU3CcGFM"
GITHUB_REPO = "https://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@github.com/Benner13/rav-tracker.git"
LOCAL_DIR = "rav-tracker"
CSV_FILE = "snapshot.csv"

def fetch_holders():
    url = f"https://api.step.finance/v1/tokenholders?token={TOKEN_MINT}&limit=1000"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            holders = [{"Owner": entry["holder"], "Amount": entry["amount"]} for entry in data]
            print(f"✅ {len(holders)} Wallets von Step Finance geladen.")
            return holders
        else:
            print("❌ Fehler bei Step API:", response.status_code, response.text)
            return []
    except Exception as e:
        print("❌ Fehler beim Abruf:", str(e))
        return []

def write_snapshot(holders):
    path = os.path.join(LOCAL_DIR, CSV_FILE)
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["Owner", "Amount"])
        writer.writeheader()
        writer.writerows(holders)
    print(f"✅ snapshot.csv geschrieben mit {len(holders)} Einträgen.")

def clone_repo():
    if not os.path.isdir(LOCAL_DIR):
        subprocess.run(["git", "clone", GITHUB_REPO], check=True)

def commit_and_push():
    try:
        subprocess.run(["git", "add", CSV_FILE], cwd=LOCAL_DIR, check=True)
        subprocess.run(["git", "commit", "-m", "update snapshot from Step"], cwd=LOCAL_DIR, check=True)
        subprocess.run(["git", "push"], cwd=LOCAL_DIR, check=True)
        print("✅ snapshot.csv erfolgreich gepusht.")
    except Exception as e:
        print("❌ Fehler beim Git-Push:", str(e))

def main():
    clone_repo()
    holders = fetch_holders()
    if holders:
        write_snapshot(holders)
        commit_and_push()
    else:
        print("⚠️ Keine Wallets zum Schreiben gefunden.")

if __name__ == "__main__":
    main()
