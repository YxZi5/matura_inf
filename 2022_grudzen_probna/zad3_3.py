#!/usr/bin/python3

def sito(N):
	tab = []
	for _ in range(0, N):
		tab.append(True)

	primes = []

	for i in range(0, N):
		if i <= 1:
			tab[i] = False

		if tab[i] == True:
			primes.append(i)

			for k in range(i, len(tab), i):
				tab[k] = False

	return primes


with open("Dane_2212/liczby.txt", "r") as liczby:
	liczby = liczby.read().splitlines()

dataset = {}

for liczba in liczby:
	
	l = int(liczba)

	pary = []
	pierwsze = sito(l)

	for i in range(0, len(pierwsze)):
		first = pierwsze[i]

		for k in pierwsze:
			if first + k == l:
				elem = [first, k]
				elem = sorted(elem)

				if elem not in pary:
					pary.append(elem)

	dataset[l] = len(pary)

print(dataset)

# wyniki = []

# for key, value in dataset.items():
# 	wyniki.append(value)

# max_value = max(wyniki)
# min_value = min(wyniki)

# for key, value in dataset.items():
	
# 	if value == max_value:
# 		print(f"MAX liczba: {key}, liczba rozkladow: {value}")

# 	if value == min_value:
# 		print(f"MIN liczba: {key}, liczba rozkladow: {value}")
