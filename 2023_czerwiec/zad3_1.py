#!/usr.bin/python3

zrownowazone = 0
prawie = 0

with open("DANE/DANE_M/anagram.txt") as liczby:
	liczby = liczby.read().splitlines()
	for num in liczby:
		num = str(num)
		zeros = 0
		ones = 0
		for char in num:
			if char == "0":
				zeros += 1
			else:
				ones += 1

		if zeros == ones:
			zrownowazone += 1

		if zeros == ones+1:
			prawie += 1

		if ones == zeros+1:
			prawie += 1

		zeros = 0
		ones = 0

print(f"{zrownowazone}\n{prawie}")