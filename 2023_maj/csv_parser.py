#!/usr/bin/python3

import csv

with open("Dane_2305/oceny.txt", "r") as file:
	reader = csv.reader(file, delimiter='\t')
	next(reader)

	data = []

	for row in reader:
		# id_gry, id_gracza, stan, ocena = row
		# data.append({
		# 	'id_gry': int(id_gry),
		# 	'id_gracza': int(id_gracza),
		# 	'stan': stan,
		# 	'ocena': int(ocena)
		# })
		data.append(row)

# for row in data:
# 	if row['stan'] == "posiada":
# 		print(f"Id gracza: {row['id_gracza']} | stan: {row['stan']}")

# LEGENDA OBSŁUGI PLIKU:
# 0 - id_gry
# 1 - id_gracza
# 2 - stan
# 3 - ocena

for row in data:
	print(row)
