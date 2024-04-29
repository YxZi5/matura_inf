#!/usr/bin/python3

with open("DANE/liczby.txt", "r") as file:
	file = file.read().splitlines()

num_roznicy = 0
bigest_roznica = 0

for num in file:
	odbicie = int(str(num)[::-1])
	roznica = int(num) - odbicie
	if roznica < 0:
		roznica = roznica * -1
	if roznica > bigest_roznica:
		bigest_roznica = roznica
		num_roznicy = num

print(f"{num_roznicy} {bigest_roznica}")