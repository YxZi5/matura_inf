#!/usr/bin/python3

def change_to_array(word):
	tab = []

	for i in range(0, len(word)):
		tab.append(word[i])

	return tab

def czy_mniejsz(n, s, k1, k2):
	i = k1
	j = k2
	
	while i <= n and j <= n:
		if s[i] == s[j]:
			i = i + 1
			j = j + 1
		else:
			if s[i] < s[j]:
				return True
			else:
				return False
	
	if j <= n:
		return True
	else:
		return False

with open("DANE/DANE_M/slowa2.txt", "r") as dane:
	dane = dane.read().splitlines()

n = int(dane[0])

slowo = dane[1]
slowo = change_to_array(slowo)

numbers = dane[2].split()
k1 = int(numbers[0])
k2 = int(numbers[1])

output = czy_mniejsz(n, slowo, k1, k2)
