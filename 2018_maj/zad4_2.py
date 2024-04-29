#!/usr/bin/python3

with open("DANE/sygnaly.txt") as dane:
	dane = dane.read().splitlines()

dataset = {}

for elem in dane:
	word_counter = {}

	for i in elem:
		if i in word_counter:
			word_counter[i] += 1
		else:
			word_counter[i] = 1

	counter = 0
	for key, value in word_counter.items():
		counter += 1

	if counter in dataset.values():
		continue	

	dataset[elem] = counter

max_value = max(dataset.values())

for key, value in dataset.items():
	
	if value == max_value:
		print(f"{key} {value}")
		break