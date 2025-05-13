import csv

with open("snapshot.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    print("📌 Gefundene Spalten:", reader.fieldnames)

    for i, row in enumerate(reader):
        print(f"🔹 Zeile {i+1}:", row)
        if i >= 4:
            break
