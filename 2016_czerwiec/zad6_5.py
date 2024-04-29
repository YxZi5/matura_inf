#!/usr/bin/python3

def to_dec(number):
	code = int(number[len(number)-1])
	number = number[:-1]
	decimal = int(number, code)

	return decimal

with open("liczby.txt", "r") as liczby:
	liczby = liczby.read().splitlines()

najmniejsza = -1
kod_najmniejsza = ""

najwieksza = -1
kod_najwieksza = ""

for i in range(0, len(liczby)):
	decimal = to_dec(liczby[i])

	if i == 0:
		najmniejsza = decimal
		kod_najmniejsza = liczby[i]

		najwieksza = decimal
		kod_najwieksza = liczby[i]
		continue

	if decimal > najwieksza:
		najwieksza = decimal
		kod_najwieksza = liczby[i]

	if decimal < najmniejsza:
		najmniejsza = decimal
		kod_najmniejsza = liczby[i]

print(f"Kod najmniejszej liczby: {kod_najmniejsza} | liczba dziesietna: {najmniejsza}")
print(f"Kod największej liczby: {kod_najwieksza} | liczba dziesietna: {najwieksza}")


