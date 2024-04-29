#!/usr/bin/python3
import math

# obie opcje działaja, funkcja check2() jest autorskim
# rozwiązaniem. Funkcja check() jest po czesci wygenerowana
# przez AI. Zamiast funkcji pow() można było użyć zapisu 3**i

def check2(n):
	liczba = int(n)
	for i in range(0, liczba+1):
		if liczba == pow(3, i):
			return True
		elif liczba < pow(3, i):
			return False

def check(n):
	number = int(n)
	i = 0
	while True:
		if number == pow(3, i):
			return True
		elif number < pow(3, i):
			return False

		i += 1

if __name__ == '__main__':
	counter = 0
	with open('Dane_PR/liczby.txt', 'r') as numbers:
		lines = numbers.read().splitlines()
		for num in lines:
			if check2(num) == True:
				counter += 1
	
	print(counter)
		