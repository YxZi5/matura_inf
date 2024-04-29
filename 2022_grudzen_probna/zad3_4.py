#!/usr/bin/python3

with open("Dane_2212/liczby_przyklad.txt", "r") as liczby:
	liczby = liczby.read().splitlines()

wordlist = {}

for i in range(0, 16):
	hex_v = hex(i)[2:]
	wordlist[hex_v] = 0

for num in liczby:
	hex_value = hex(int(num))[2:]

	for i in range(0, len(hex_value)):
		v = hex_value[i]

		if v in wordlist:
			wordlist[v] += 1
		else:
			wordlist[v] = 1

for key, value in wordlist.items():
	print(f"{key}:{value}")