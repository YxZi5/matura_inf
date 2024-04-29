#!/usr/bin/python3

with open("Dane_2212/pary.txt") as pary:
	pary = pary.read().splitlines()


for row in pary:
	tab = row.split()

	x = int(tab[0])
	y = int(tab[1])

	y_copy = y

	while True:

		if x >= y:
			break

		y = y // 2

	if x == y:
		print(f"{x} --> {y_copy}")