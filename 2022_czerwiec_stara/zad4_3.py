#!/usr/bin/python3

def is_prime(x):
	if x > 1:
		if x == 2:
			return True
		if x % 2 == 0 or x <= 1:
			return False

		for dzielnik in range(3, x):
			if x % dzielnik == 0:
				return False
		return True
	return False

with open("DANE/liczby.txt", "r") as file:
	file = file.read().splitlines()

for num in file:
	odbicie = int(str(num)[::-1])
	num = int(num)
	if is_prime(num) == True and is_prime(odbicie) == True:
		print(num)

