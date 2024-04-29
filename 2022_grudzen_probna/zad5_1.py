#!/usr/bin/python3
import csv
from datetime import datetime


def roznica_dni(data_poczatek, data_koniec):
	data_poczatek = datetime.strptime(data_poczatek, "%Y-%m-%d")
	data_koniec = datetime.strptime(data_koniec, "%Y-%m-%d")

	roznica = data_koniec - data_poczatek

	return roznica

dataset = {}

with open("Dane_2212/klienci.txt", "r") as klienci:
	klienci = csv.reader(klienci, delimiter="	")
	next(klienci)

	klienci_dane = []

	for row in klienci:
		nr_dowodu = row[0]
		imie = row[2]
		nazwisko = row[1]

		elem = [nr_dowodu, imie, nazwisko]

		dataset[nr_dowodu] = 0
		klienci_dane.append(elem)


with open("Dane_2212/noclegi.txt", "r") as noclegi:
	noclegi = csv.reader(noclegi, delimiter="	")
	next(noclegi)

	noclegi_dane = []

	for row2 in noclegi:
		od = row2[1]
		do = row2[2]
		pobyt_dni = roznica_dni(od, do).days

		nr_dowodu = row2[3]
		
		elem = [nr_dowodu, pobyt_dni]
		noclegi_dane.append(elem)


for elem in noclegi_dane:
	dataset[elem[0]] += elem[1]

values = []
for key, value in dataset.items():
	values.append(value)

max_value = max(values)

for key, value in dataset.items():
	if value == max_value:
		
		for i in klienci_dane:
			if i[0] == key:
				imie = i[1]
				nazwisko = i[2]
				print(f"{imie} {nazwisko} liczba noclegow: {value}")