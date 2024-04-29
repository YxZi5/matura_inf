#!/usr/bin/python3

with open("liczby.txt", "r") as liczby:
	liczby = liczby.read().splitlines()

count = 0
binarne = []

for num in liczby:
	
	if num[len(num)-1] != "2":
		continue

	decimal = num[:-1]
	decimal = int(decimal, 2)

	if decimal % 2 == 0:
		count += 1

print(count)