#!/usr/bin/python3

def blocks(binary_number):
	blocks_num = 1
	for k in range(0, len(binary_number)):
		if k == 0:
			continue

		if binary_number[k] != binary_number[k-1]:
			# print(f"k = {k}")
			blocks_num += 1

	return blocks_num

with open("Dane_2305/bin.txt", "r") as file:
	file = file.read().splitlines()

counter = 0

for line in file:
	blocks_n = blocks(line)
	if blocks_n <= 2:
		counter += 1

print(counter)