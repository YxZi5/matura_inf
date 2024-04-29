#!/usr/bin/python3

with open("punkty.txt", "r") as punkty:
	punkty = punkty.read().splitlines()

inside = 0
na_bokach = 0
outside = 0

for line in punkty:
	tab = line.split()
	
	x = int(tab[0])
	y = int(tab[1])

	if x < 5000 and y < 5000:
		inside += 1

	if x == 5000 or y == 5000:
		na_bokach += 1

	if x > 5000 or y > 5000:
		outside += 1

print(f"Wewnatrz kwadratu: {inside} | na bokach: {na_bokach} | na zewnatrz: {outside}")