#!/usr/bin/python3

def silnia(n):
	if n < 0:
		return None
	elif n == 0:
		return 1
	else:
		wynik = 1
		for i in range(1, n+1):
			wynik *= i
		return wynik

if __name__ == '__main__':
	counter = 0
	with open('Dane_PR/liczby.txt', 'r') as numbers:
		numbers = numbers.read().splitlines()
		for num in numbers:
			wynik = 0
			for digit in str(num):
				wynik += silnia(int(digit))
			# print(f"Wynik: {wynik}")
			if int(num) == wynik:
				print(num)
				# counter += 1

	# print(counter)