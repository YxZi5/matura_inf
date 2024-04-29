#!/usr/bin/python3

def is_zero(number):
	for i in range(0, len(number)):
		if number[i] == "0":
			return True

	return False

with open("liczby.txt", "r") as liczby:
	liczby = liczby.read().splitlines()

count = 0

for num in liczby:
	if num[len(num)-1] != "4":
		continue

	if is_zero(num) == False:
		# print(num)
		count += 1

print(count)