#!/usr/bin/python3

def pierwsza(liczba):

	if liczba == 2:
		return True

	if liczba == 1:
		return False

	if liczba % 2 == 0:
		return False

	if liczba > 2:	
		for i in range(2, liczba-1):
			
			if liczba % i == 0:
				return False

		return True

with open("punkty.txt", "r") as punkty:
	punkty = punkty.read().splitlines()

counter = 0

for linia in punkty:
	tab = linia.split()

	l1 = int(tab[0])
	l2 = int(tab[1])

	if pierwsza(l1) == True and pierwsza(l2) == True:
		counter += 1

print(counter)