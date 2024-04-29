#!/usr/bin/python3
import csv

with open("programy.txt", "r") as programy:
	programy = csv.reader(programy, delimiter="	")
	next(programy)

	programs = []

	for row in programy:

		if "zarzadzanie" not in row[2]:
			continue

		idd = row[0]
		program_name = row[1]

		elem = [idd, program_name]
		programs.append(elem)


with open("zestawy.txt", "r") as zestawy:
	zestawy = csv.reader(zestawy, delimiter="	")
	next(zestawy)

	id_pakietow = []

	for row2 in zestawy:
		id_pakietu = row2[0]
		id_programu = row2[1]

		for i in range(0, len(programs)):

			if id_programu == programs[i][0]:
				id_pakietow.append(id_pakietu)


pakiety_programow = {}

with open("pakiety.txt", "r") as pakiety:
	pakiety = csv.reader(pakiety, delimiter="	")
	next(pakiety)

	for row3 in pakiety:
		id_pakietu = row3[0]
		nazwa_pakietu = row3[1]

		for k in range(0, len(id_pakietow)):
			
			if id_pakietu == id_pakietow[k]:
				if nazwa_pakietu in pakiety_programow:
					pakiety_programow[nazwa_pakietu] += 1
				else:
					pakiety_programow[nazwa_pakietu] = 1


for pakiet, ilosc in pakiety_programow.items():
	print(pakiet)
