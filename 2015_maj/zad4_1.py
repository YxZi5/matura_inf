#!/usr/bin/python3

with open("dane/liczby.txt", "r") as numbers:
	numbers = numbers.read().splitlines()


counter = 0

for i in range(0, len(numbers)):
	zera = 0
	jedynki = 0

	str_number = str(numbers[i])

	for char in str_number:
		if char == "0":
			zera += 1

		if char == "1":
			jedynki += 1


	if zera > jedynki:
		# print(str_number)
		counter += 1

print(counter)