#!/usr/bin/python3

with open("Dane_2212/mecz_przyklad.txt", "r") as mecz:
	file = mecz.read().splitlines()

teamA = 0
teamB = 0

for char in file[0]:
	if teamA >= 1000 or teamB >= 1000:
		if teamA > teamB:
			print(f"A {teamA}:{teamB}")
		else:
			print(f"B {teamB}:{teamA}")
		break

	if char == "A":
		teamA += 1

	if char == "B":
		teamB += 1
