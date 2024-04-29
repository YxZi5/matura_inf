#!/usr/bin/python3
import csv

def find_top_4(data):
	all_ceny = []

	for id_pakietu, suma_cen in data.items():
		all_ceny.append(suma_cen)

	all_ceny = sorted(all_ceny)[::-1]
	top_4 = []

	for i in range(0, 3):
		top_4.append(all_ceny[i])

	return top_4

with open("zestawy.txt", "r") as zestawy:
	zestawy = csv.reader(zestawy, delimiter="	")
	next(zestawy)

	pakietID_programID = []

	for row in zestawy:
		id_pakietu = row[0]
		id_programu = row[1]

		elem = [id_pakietu, id_programu]
		pakietID_programID.append(elem)


sumy_cen_dla_pakietowID = {}

with open("programy.txt", "r") as programy:
	programy = csv.reader(programy, delimiter="	")
	next(programy)

	for row2 in programy:
		id_programu = row2[0]
		cena_programu = int(row2[3])

		for i in range(0, len(pakietID_programID)):

			id_pakietu = pakietID_programID[i][0]

			if pakietID_programID[i][1] != id_programu:
				continue

			if id_pakietu in sumy_cen_dla_pakietowID:
				sumy_cen_dla_pakietowID[id_pakietu] += cena_programu
			else:
				sumy_cen_dla_pakietowID[id_pakietu] = 1


top_4_sumy = find_top_4(sumy_cen_dla_pakietowID)

id_suma_top4 = []

for id_pakietu, suma_cen in sumy_cen_dla_pakietowID.items():
	
	for i in range(0, len(top_4_sumy)):
		if suma_cen == top_4_sumy[i]:
			elem = [id_pakietu, suma_cen]
			id_suma_top4.append(elem)

id_suma_top4 = id_suma_top4[::-1]


with open("pakiety.txt", "r") as pakiety:
	pakiety = csv.reader(pakiety, delimiter="	")
	next(pakiety)

	for row3 in pakiety:
		idd = row3[0]
		nazwa_pakietu = row3[1]
		nazwa_firmy = row3[2]

		for k in range(0, len(id_suma_top4)):
			
			if id_suma_top4[k][0] == idd:
				suma_cen = id_suma_top4[k][1]
				print(f"Nazwa: {nazwa_pakietu}, Firma: {nazwa_firmy}, wartosc: {suma_cen}")
