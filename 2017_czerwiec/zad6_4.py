#!/usr/bin/python3
import csv

with open("programy.txt", "r") as programy:
	programy = csv.reader(programy, delimiter="	")
	next(programy)

	id_nazwa_programu = []

	for row in programy:
		id_programu = row[0]
		nazwa_programu = row[1]

		elem = [id_programu, nazwa_programu]

		id_nazwa_programu.append(elem)

zestawy_id_programow = []

with open("zestawy.txt", "r") as zestawy:
	zestawy = csv.reader(zestawy, delimiter="	")
	next(zestawy)

	for row2 in zestawy:
		zestawy_id_programu = row2[1]
		zestawy_id_programow.append(zestawy_id_programu)

for i in range(0, len(id_nazwa_programu)):
	
	if id_nazwa_programu[i][0] not in zestawy_id_programow:
		print(id_nazwa_programu[i][1])