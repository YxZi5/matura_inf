#!/usr/bin/python3

def czy_rozne(num_string):
	for i in range(0, len(num_string)):
		for j in range(i+1, len(num_string)):
			if num_string[i] == num_string[j]:
				return False

	return True

# zamiana wszystkich liczb na dziesietny i dodanie do listy
dec_numbers = []

with open("DANE/DANE_M/anagram.txt") as liczby:
	liczby = liczby.read().splitlines()
	for num in liczby:
		n = int(num, 2)
		dec_numbers.append(n)


# a:
counter = 0
for n in range(0, len(dec_numbers)):
	s = str(dec_numbers[n])
	if "0" in s:
		continue
	else:
		counter += 1

# b:
bigest_sum = 0
best = ""

for n in range(0, len(dec_numbers)):
	suma = 0
	s = str(dec_numbers[n])
	
	if czy_rozne(s) == True:
		for char in s:
			suma += int(char)

		if suma > bigest_sum:
			bigest_sum = suma
			best = s

print(counter)
print(best)