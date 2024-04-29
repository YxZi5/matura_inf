#!/usr/bin/python3

with open("DANE/dane.txt", "r") as pixele:
	pixele = pixele.read().splitlines()

dataset = []

dlugosci = []

for row in pixele:
	row = row.split()
	dataset.append(row)

for i in range(0, 200):
	
	dlugosc_kolumny = 1
	
	for k in range(0, len(dataset)):

		if k == len(dataset)-1:
			break

		if int(dataset[k][i]) == int(dataset[k+1][i]):
			dlugosc_kolumny += 1
		else:
			dlugosci.append(dlugosc_kolumny)
			dlugosc_kolumny = 1

max_value = sorted(dlugosci)[len(dlugosci)-1]
print(max_value)
