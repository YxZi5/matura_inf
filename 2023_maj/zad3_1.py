#!/usr/bin/python3

with open("Dane_2305/pi.txt", "r") as file:
	file = file.read().splitlines()

counter = 0

for line in range(0, len(file)-1):
	acctual_num = file[line]+file[line+1]
	acctual_num = int(acctual_num)

	if acctual_num > 90:
		counter += 1

print(counter)