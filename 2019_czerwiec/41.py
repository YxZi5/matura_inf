#!/usr/bin/python3

def load_pierwsze():
	pierwsze = []
	plik_pierwsze = open('pierwsze.txt', 'r')

	for pierwsza in plik_pierwsze:
		pierwsza = pierwsza.strip()
		pierwsze.append(pierwsza)

	return pierwsze

if __name__ == '__main__':
	pierwsze = load_pierwsze()
	with open('liczby.txt', 'r') as liczby:
		liczby = liczby.read().splitlines()

		for i in range(len(liczby)):
			if int(liczby[i]) > 100 and int(liczby[i]) < 5000:
				for pierwsza in pierwsze:
					if liczby[i] == pierwsza:
						print(liczby[i])