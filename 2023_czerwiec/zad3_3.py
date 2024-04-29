#!/usr/bin/python3

with open("DANE/DANE_M/przyklad.txt") as liczby:
	liczby = liczby.read().splitlines()

bigest = 0

for i in range(0, len(liczby), 2):
	n1 = int(liczby[i], 2)
	n2 = int(liczby[i+1], 2)
	if n1 > n2:
		o = n1 - n2
	
	if n2 > n1:
		o = n2 - n1

	if o > bigest:
		bigest = o

print(bin(bigest)[2::])