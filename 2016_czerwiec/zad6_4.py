#!/usr/bin/python3

with open("liczby.txt", "r") as liczby:
	liczby = liczby.read().splitlines()

suma = 0

for num in liczby:
	
	if num[len(num)-1] != "8":
		continue

	octal_num = num[:-1]
	decimal = int(octal_num, 8)
	suma += decimal

print(suma)