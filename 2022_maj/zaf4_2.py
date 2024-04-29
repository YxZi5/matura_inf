#!/usr/bin/python3

def factors(x):
	out = []
	k = 2
	while x != 1:
		while x % k == 0:
			x //= k
			# print(k)
			out.append(k)
		k += 1
	return out

def powtarzaja_sie(czynniki):
	k = 0
	for i in range(0, len(czynniki)-1):
		if czynniki[i] == czynniki[k+1]:
			return True
		else:
			k += 1

	return False

def rozne_czynniki(liczby):
	ktora = 0
	max_ilosc_czynikow = 0
	for i in range(0, len(liczby)):
		czynniki = factors(int(liczby[i]))
		if powtarzaja_sie(czynniki) != True:
			if len(czynniki) > max_ilosc_czynikow:
				max_ilosc_czynikow = len(czynniki)
				ktora = int(liczby[i])
	return ktora

def najwiecej_czynnikow(liczby):
	ktora_liczba = 0
	ilosc_czynikow = 0

	for i in range(0, len(liczby)):
		ile_czynikow_liczba = len(factors(int(liczby[i])))
			
		if ile_czynikow_liczba > ilosc_czynikow:
			ilosc_czynikow = ile_czynikow_liczba
			ktora_liczba = int(liczby[i])

	return ktora_liczba;

if __name__ == '__main__':
	with open('Dane_2205/przyklad.txt', 'r') as file:
		linie = file.read().splitlines()

		najwiecej_liczba = najwiecej_czynnikow(linie)
		liczba_czynnikow = len(factors(najwiecej_liczba))

		najwiecej_roznych = rozne_czynniki(linie)
		liczba_czynnikow2 = len(factors(najwiecej_roznych))

		file.close()

	print(f"{najwiecej_liczba} {liczba_czynnikow} {najwiecej_roznych} {liczba_czynnikow2}")