#!/usr/bin/python3

import csv

with open("Dane_2305/oceny.txt", "r") as file:
	reader = csv.reader(file, delimiter='\t')
	next(reader)

	data = []

	for row in reader:
		data.append(row)

# LEGENDA OBSŁUGI PLIKU:
# 0 - id_gry
# 1 - id_gracza
# 2 - stan
# 3 - ocena

counter = {}

for row in data:
	id_gry = row[0]
	# ocena = row[3]
	if id_gry in counter:
		counter[id_gry] += 1
	else:
		counter[id_gry] = 1

bigest_value = max(counter, key=counter.get)
file.close()

# open file gry.txt and find game name with finded id
with open("Dane_2305/gry.txt", "r") as gry:
	reader = csv.reader(gry, delimiter='\t')
	next(reader)

	gry_list = []

	for row in reader:
		gry_list.append(row)

	# id - 0
	# nazwa - 1
	# kategoria - 2

	for line in gry_list:
		if line[0] == bigest_value:
			print(line[1])
