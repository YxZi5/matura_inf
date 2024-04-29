#!/usr/bin/python3

with open("Dane_2305/bin_przyklad.txt", "r") as file:
	file = file.read().splitlines()

bigest_value = 0

for line in file:
	dec_value = int(line, 2)
	if dec_value > bigest_value:
		bigest_value = dec_value

binn = bin(bigest_value).replace("0b", "")
print(binn)