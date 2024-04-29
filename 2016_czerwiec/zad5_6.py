#!/usr/bin/python3
import csv

with open("maturzysta.txt", "r") as maturzysci:
	maturzysci = csv.reader(maturzysci, delimiter=";")
	next(maturzysci)

	pesele = []
	for row in maturzysci:
		pesele.append(row[3])

counter = 0

for i in range(0, len(pesele)):
	reversed_pesel = pesele[i][::-1]
	
	if int(reversed_pesel[1]) % 2 != 0:
		counter += 1

print(counter)
