#!/usr/bin/python3

with open("DANE/sygnaly.txt") as dane:
	dane = dane.read().splitlines()

tab = []

for i in range(0, len(dane)+1, 40):
	if i == 0:
		continue

	# print(f"{i} => {dane[i-1]}")
	tab.append(dane[i-1])

output = ""

for elem in tab:
	letter = elem[9]
	output += letter

print(output)
