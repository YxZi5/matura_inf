#!/usr/bin/python3

with open("Dane_2212/mecz.txt", "r") as mecz:
	file = mecz.read().splitlines()

counter = 0

for i in range(0, len(file[0])):
	if i == 0:
		continue

	acctual_char = file[0][i]
	previous = file[0][i-1]

	if acctual_char != previous:
		counter += 1


print(counter)