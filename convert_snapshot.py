import csv

with open("snapshot.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    print("📌 Feldnamen gefunden:", reader.fieldnames)

    wallets = []
    for i, row in enumerate(reader):
        print(f"🔹 Zeile {i+1}: {row}")
        if row.get("holder"):
            wallets.append(row["holder"])

with open("walletlist.txt", "w") as f:
    for wallet in wallets:
        f.write(wallet + "\n")

print(f"✅ walletlist.txt mit {len(wallets)} Einträgen erstellt.")
