#!/usr/bin/python3

with open("DANE/przyklad.txt", "r") as pixele:
	pixele = pixele.read().splitlines()

counter = 0

for row in pixele:

	row = row.split()
	for i in range(0, len(row)):
		if row[i] != row[319-i]:
			counter += 1
			break

print(counter)