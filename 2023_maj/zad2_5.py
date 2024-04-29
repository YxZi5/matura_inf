#!/usr/bin/python3

with open("Dane_2305/bin.txt", "r") as file:
	file = file.read().splitlines()

wynik = open("wyniki2_5.txt", "w")

for line in file:
	p = int(line, 2)

	# polowa liczby:
	s = p / 2
	s = str(s).split(".")[0]

	xored = p ^ int(s)
	xored_bin = bin(xored)
	xored_bin = xored_bin[2:]

	wynik.write(xored_bin+"\n")