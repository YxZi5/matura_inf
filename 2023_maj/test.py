#!/usr/bin/python3

with open("a.txt", "r") as a:
	a = a.read().splitlines()


tab = a[0].split()

tab_v2 = []

for i in range(0, len(tab)):
	int_value = int(tab[i])
	tab_v2.append(int_value)

print(max(tab_v2))