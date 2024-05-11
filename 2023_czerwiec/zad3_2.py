#!/usr/bin/python3


def count_zeros(num):
	c = 0
	for char in num:
		if char == "0":
			c += 1
	return c

def count_ones(num):
	c = 0
	for char in num:
		if char == "1":
			c += 1
	return c

with open("DANE/DANE_M/przyklad.txt") as liczby:
	liczby = liczby.read().splitlines()

	# find only nums with 8 length and starts from 1
	byte_len_nums = []

	for num in liczby:
		if len(num) == 8 and num[0] == "1":
			byte_len_nums.append(num)


# for n in range(0, len(byte_len_nums)):	
# 	j = count_ones(byte_len_nums[n])
# 	z = count_zeros(byte_len_nums[n])
# 	for n2 in range(n, len(byte_len_nums)):
# 		j2 = count_ones(byte_len_nums[n2])
# 		z2 = count_zeros(byte_len_nums[n2])

# 		if j == j2 and z == z2:
# 			# print(byte_len_nums[n])
# 			print(byte_len_nums[n2])

print(byte_len_nums)
