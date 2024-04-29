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

def load_pierwsze():
	pierwsze = []
	plik_pierwsze = open('pierwsze_przyklad.txt', 'r')

	for pierwsza in plik_pierwsze:
		pierwsza = pierwsza.strip()
		pierwsze.append(pierwsza)

	return pierwsze

if __name__ == '__main__':
	pierwsze = load_pierwsze()
	for i in range(len(pierwsze)):
		pierwsza_right = str(pierwsze[i])
		pierwsza_right = pierwsza_right[::-1]
		
		if is_prime(int(pierwsza_right)) == True:
			print(pierwsze[i])