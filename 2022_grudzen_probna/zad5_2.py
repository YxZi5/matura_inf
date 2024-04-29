#!/usr/bin/python3
import csv
from datetime import datetime

def roznica_dni(data_poczatek, data_koniec):
	data_poczatek = datetime.strptime(data_poczatek, "%Y-%m-%d")
	data_koniec = datetime.strptime(data_koniec, "%Y-%m-%d")

	roznica = data_koniec - data_poczatek

	return roznica

with open("Dane_2212/klienci.txt", "r") as klienci:
	klienci = csv.reader(klienci, delimiter="	")
	next(klienci)

	klienci_dane = []

	for row in klienci:
		imie = row[2]
		nazwisko = row[1]
		nr_dowodu = row[0]

		elem = [imie, nazwisko, nr_dowodu]

		klienci_dane.append(elem)


with open("Dane_2212/noclegi.txt", "r") as noclegi:
	noclegi = csv.reader(noclegi, delimiter="	")
	next(noclegi)

	noclegi_dane = []

	for row2 in noclegi:
		nr_dowodu = row2[3]
		nr_pokoju = row2[4]

		od = row2[1]
		do = row2[2]

		ile_dni = roznica_dni(od, do).days

		elem = [nr_dowodu, nr_pokoju, ile_dni]

		noclegi_dane.append(elem)


ile_zaplacili = {}

for i in range(0, len(klienci_dane)):
	nr_dowodu = klienci_dane[i][2]

	ile_zaplacili[nr_dowodu] = 0

with open("Dane_2212/pokoje.txt", "r") as pokoje:
	pokoje = csv.reader(pokoje, delimiter="	")
	next(pokoje)

	for row3 in pokoje:
		nr_pokoju = row3[0]
		cena = int(row3[2])

		for i in range(0, len(noclegi_dane)):
			nr_pokoju_noclegi_dane = noclegi_dane[i][1]
			nr_dowodu = noclegi_dane[i][0]
			ile_dni = int(noclegi_dane[i][2])

			if nr_pokoju == nr_pokoju_noclegi_dane:
				ile_zaplacili[nr_dowodu] += (cena*ile_dni)

# szukanie osob powyzej 2000

ceny = []
for dowod, cena in ile_zaplacili.items():
	if cena > 2000:
		ceny.append(cena)

ceny = sorted(ceny)

final_dataset = []
for dowod, cena in ile_zaplacili.items():
	if cena in ceny:
		elem = [dowod, cena]
		final_dataset.append(elem)

for row in klienci_dane:
	for elem in final_dataset:
		if row[2] == elem[0]:
			print(f"{row[0]} {row[1]} - {elem[1]}zł")