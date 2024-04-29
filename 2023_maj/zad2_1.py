#!/usr/bin/python3

# to zadanie powinno być w pseudokodzie, jednak w zadaniu pisało że "lub"
# w wybranym języku programowania

def dec2bin(number):
	binary = ""
	while number != 0:
		binary += str(number%2)
		number = int(number / 2)

	# reverse binary number
	binary_2 = ""
	for i in range(len(binary)-1, -1, -1):
		binary_2 += binary[i]

	return binary_2

# calculate nums of blocks in binary representation

binary_number = dec2bin(31799)

blocks_num = 1
for k in range(0, len(binary_number)):
	if k == 0:
		continue

	if binary_number[k] != binary_number[k-1]:
		print(f"k = {k}")
		blocks_num += 1

print(blocks_num)