#!/usr/bin/python3

import csv

with open("DANE/sedziowie.txt", "r") as sedziowie:
	sedziowie = csv.reader(sedziowie, delimiter="	")
	next(sedziowie)

	sedziowie_data = []

	for row in sedziowie:
		sedziowie_data.append(row)

sedziowie_dataset = {}

for row in sedziowie_data:
	nr_licencji = row[0]
	sedziowie_dataset[nr_licencji] = 0

with open("DANE/wyniki.txt", "r") as wyniki:
	wyniki = csv.reader(wyniki, delimiter="	")
	next(wyniki)

	wyniki_data = []

	for row in wyniki:
		wyniki_data.append(row)

for row2 in wyniki_data:
	nr = row2[4]
	rodzaj_meczu = row2[1]

	if rodzaj_meczu != "P":
		continue

	sedziowie_dataset[nr] += 1

ile_zero = []

for key, value in sedziowie_dataset.items():

	if value == 0:
		ile_zero.append(key)

print(len(ile_zero))