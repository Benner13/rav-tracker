import csv

with open("snapshot.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)

    if "holder" not in reader.fieldnames:
        print(f"❌ Fehler: Spalte 'holder' nicht gefunden! Stattdessen gefunden: {reader.fieldnames}")
        exit(1)

    wallets = [row["holder"] for row in reader if row.get("holder")]

with open("walletlist.txt", "w") as f:
    for wallet in wallets:
        f.write(wallet + "\n")

print(f"✅ walletlist.txt mit {len(wallets)} Einträgen erstellt.")
