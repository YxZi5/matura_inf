#!/usr/bin/python3

def czy_pierwsza(x):
	if x == 0:
		return False

	if x == 1:
		return False

	if x == 2:
		return True

	if x > 2:
		for k in range(2, x):
			if x % k == 0:
				return False

		return True

with open("Dane_2212/liczby.txt", "r") as liczby:
	liczby = liczby.read().splitlines()

counter = 0

for i in range(0, len(liczby)):
	liczba = int(liczby[i]) - 1

	if czy_pierwsza(liczba) == True:
		counter += 1

print(counter)