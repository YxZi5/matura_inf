#!/usr/bin/python3

import csv

with open("Dane_2305/oceny.txt", "r") as file:
	reader = csv.reader(file, delimiter='\t')
	next(reader)

	dane_all = []
	len_all = 0

	for row in reader:
		len_all += 1
		dane_all.append(row)

	gracze = {}

	for row in dane_all:
		id_gracza = row[1]
		game_status = row[2]

		if id_gracza in gracze:
			if game_status == "posiada":
				gracze[id_gracza] += 1
		else:
			if game_status == "posiada":
				gracze[id_gracza] = 1

	# for id_gracza, liczba_gier in gracze.items():
		# print(f"Gracz o ID: {id_gracza} posiada: {liczba_gier} gier)"
	
	liczba_bez_gier = len_all = len(gracze)
	print(len_all)