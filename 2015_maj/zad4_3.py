#!/usr/bin/python3

with open("dane/liczby.txt", "r") as numbers:
	numbers = numbers.read().splitlines()

najmniejsza = -1
najmniejsza_line = 0

najwieksza = -1
najwieksza_line = 0

for i in range(0, len(numbers)):
	wiersz = i+1
	dec_num = int(str(numbers[i]), 2)

	if i == 0:
		najmniejsza = dec_num
		najmniejsza_line = wiersz

		najwieksza = dec_num
		najwieksza_line = wiersz
		continue

	if dec_num > najwieksza:
		najwieksza = dec_num
		najwieksza_line = wiersz

	if dec_num < najmniejsza:
		najmniejsza = dec_num
		najmniejsza_line = wiersz

najmniejsza = int(najmniejsza)
najmniejsza = bin(najmniejsza)[2::]

najwieksza = int(najwieksza)
najwieksza = bin(najwieksza)[2::]

print(f"najmniejsza liczba to: {najmniejsza} | linia: {najmniejsza_line}")
print(f"Najwieksza liczba to: {najwieksza} | linia: {najwieksza_line}")