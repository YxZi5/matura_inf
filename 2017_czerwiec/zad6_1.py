#!/usr/bin/python3
import csv

with open("programy.txt", "r") as programy:
	programy = csv.reader(programy, delimiter="	")
	next(programy)

	programs = []

	for row in programy:

		if row[2] != "edytor dokumentow tekstowych":
			continue

		idd = row[0]
		program_name = row[1]
		cena = row[3]

		elem = [idd, program_name, cena]
		programs.append(elem)

with open("zestawy.txt", "r") as zestawy:
	zestawy = csv.reader(zestawy, delimiter="	")
	next(zestawy)

	zestawy_id_programow = {}

	for row2 in zestawy:
		i = row2[1]

		if i in zestawy_id_programow:
			zestawy_id_programow[i] += 1
		else:
			zestawy_id_programow[i] = 1


for idd, ile_razy in zestawy_id_programow.items():
	
	if ile_razy < 2:
		continue

	for i in range(0, len(programs)):
		program_id = programs[i][0]

		if idd == program_id:
			program_name = programs[i][1]
			program_cost = programs[i][2]
			print(f"program: {program_name} | cena: {program_cost} | liczba pakietow: {ile_razy}")
