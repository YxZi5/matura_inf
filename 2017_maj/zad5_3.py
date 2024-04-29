#!/usr/bin/python3

import csv

with open("DANE/wyniki.txt", "r") as wyniki:
	wyniki = csv.reader(wyniki, delimiter="	")
	next(wyniki)

	wyniki_data = []

	for row in wyniki:
		wyniki_data.append(row)

wygrane = 0
przegrane = 0
zremisowane = 0

for row in wyniki_data:
	
	if row[2] != "W":
		continue

	bramki_zdobyte = row[5]
	bramki_stracone = row[6]

	if bramki_stracone == bramki_zdobyte:
		zremisowane += 1

	if bramki_zdobyte > bramki_stracone:
		wygrane += 1

	if bramki_stracone > bramki_zdobyte:
		przegrane += 1

print(f"wygrane: {wygrane}")
print(f"przegrane: {przegrane}")
print(f"zremisowane: {zremisowane}")