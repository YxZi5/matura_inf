#!/usr/bin/python3

def jaka_odleglosc(a, b):
	alfavet = gen_alfabet()

	for i in range(0, len(alfavet)):
		if alfavet[i] == a:
			first = i + 1

		if alfavet[i] == b:
			second = i + 1

	if first == second:
		return 0

	if first > second:
		return first - second

	if first < second:
		return second - first

def gen_alfabet():
	Alfabet = []

	for i in range(65, 91):
		letter = chr(i)
		Alfabet.append(letter)

	return Alfabet

def word_10(word):
	for char in word:

		for i in range(0, len(word)):
			odleglosc = jaka_odleglosc(char, word[i])

			if odleglosc > 10:
				return 0

	return 1

with open("DANE/sygnaly.txt") as dane:
	dane = dane.read().splitlines()

for elem in dane:
	
	if word_10(elem) == 1:
		print(elem)



