#!/usr/bin/python3

with open("DANE/liczby.txt", "r") as file:
	file = file.read().splitlines()

for num in file:
	num_str = str(num)
	odbicie = num_str[::-1]
	if int(odbicie) % 17 == 0:
		print(odbicie)