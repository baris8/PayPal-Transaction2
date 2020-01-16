import csv

filename = input("Bitte geben sie die CSV an:\n")

with open(filename+".csv", newline='', errors="ignore") as csvfile:
    reader = csv.reader(csvfile)

    header = next(reader)
    data = []

    for row in reader:
        if row[4] == "eBay-Auktionszahlung":
            datum = row[0]
            uhrzeit = row[1]
            name = row[3]
            typ = row[4]
            status = row[5]
            waehrung = row[6]

            brutto = float(row[7].replace(",", "."))
            netto = round(brutto/1.19, 2)
            ust = 19.00

            absender = row[10]
            empfaenger = row[11]
            transaktionscode = row[12]
            lieferadresse = row[13]

            artikelbez = row[15]
            artikelnr = row[16]

            data.append([datum, uhrzeit, name, typ, status, waehrung, brutto, netto, ust, absender, empfaenger, transaktionscode, lieferadresse, artikelbez, artikelnr])

    with open("PayPal - September.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["Datum", "Uhrzeit", "Name", "Typ", "Status", "Währung", "Brutto", "Netto", "Ust.", "Absender", "Empfänger", "Transaktionscode", "Lieferadresse", "Artikelbezeichnung", "Artikelnummer"])
        for row in data:
            writer.writerow(row)
