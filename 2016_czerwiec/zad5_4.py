#!/usr/bin/python3
import csv

with open("zdaje.txt", "r") as zdaje:
	zdaje = csv.reader(zdaje, delimiter=";")
	next(zdaje)

	egzaminy = []
	for row in zdaje:
		egzaminy.append(row[1])

with open("przedmioty.txt", "r") as przedmioty:
	przedmioty = csv.reader(przedmioty, delimiter=";")
	next(przedmioty)

	subjects = []
	for row in przedmioty:
		subjects.append(row[0])

for i in range(0, len(subjects)):
	if subjects[i] not in egzaminy:
		print(subjects[i])