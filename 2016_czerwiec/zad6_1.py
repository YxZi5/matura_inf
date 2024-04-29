#!/usr/bin/python3

with open("liczby.txt", "r") as liczby:
	liczby = liczby.read().splitlines()

count = 0

for num in liczby:
	if num[len(num)-1] == "8":
		count += 1

print(count)