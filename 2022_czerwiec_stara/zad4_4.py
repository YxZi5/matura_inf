#!/usr/bin/python3

with open("DANE/przyklad.txt", "r") as file:
	file = file.read().splitlines()

liczby = {}

for num in file:
	if num in liczby:
		liczby[num] += 1
	else:
		liczby[num] = 1

rozne = len(liczby)
repeat_2 = 0
repeat_3 = 0

for n in liczby:
	if liczby[n] == 2:
		repeat_2 += 1

	if liczby[n] == 3:
		repeat_3 += 1

print(f"{rozne} {repeat_2} {repeat_3}")