#!/usr/bin/python3

if __name__ == '__main__':
	with open('Dane_2205/przyklad.txt', 'r') as file:
		linie = file.read().splitlines()
		pierwsza = []
		ilosc = 0

		for i in range(0, len(linie)):
			liczba = str(linie[i])

			if (liczba[0] == liczba[len(liczba)-1]):
				ilosc += 1
				if len(pierwsza) == 0:
					pierwsza.append(liczba)

		file.close()

	print(f"{ilosc} {pierwsza[0]}")