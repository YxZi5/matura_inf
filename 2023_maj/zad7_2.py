#!/usr/bin/python3

import csv

with open("Dane_2305/gry.txt", "r") as file:
	reader = csv.reader(file, delimiter='\t')
	next(reader)

	gry_list = []

	for row in reader:
		gry_list.append(row)

	imprezowe = []
	for gra in gry_list:
		if gra[2] == "imprezowa":
			imprezowe.append(gra)

	file.close()

with open("Dane_2305/oceny.txt", "r") as oceny:
	reader = csv.reader(oceny, delimiter='\t')
	next(reader)

	imprezowe_oceny = []
	srednie = []

	for row in reader:
		for g in imprezowe:
			if g[0] == row[0]:
				imprezowe_oceny.append(row)

	oceny_gier = {}

	for row in imprezowe_oceny:
		game_id = row[0]
		ocena = int(row[3])
		if game_id in oceny_gier:
			oceny_gier[game_id].append(ocena)
		else:
			oceny_gier[game_id] = [ocena]

	# for game_id, oceny in oceny_gier.items():
	# 	srednia_ocen = sum(oceny) / len(oceny)
	# 	srednia_ocen = round(srednia_ocen, 2)
		# print(f"ID gry: {game_id}, średnia ocen: {srednia_ocen}")

	for item in oceny_gier.items():
		print(item)
