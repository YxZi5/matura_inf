#!/usr/bin/python3

def parse_file():
	num_strings = []
	
	with open("Dane_2305/pi_przyklad.txt", "r") as file:
		file = file.read().splitlines()
		
	for line in range(0, len(file)-5):
		acctual_str = f"{file[line]}{file[line+1]}{file[line+2]}{file[line+3]}{file[line+4]}{file[line+5]}"
		num_strings.append(acctual_str)

	return num_strings

def check_num(number):
	first3 = False
	last3 = False

	if int(number[0]) < int(number[1]) and int(number[1]) <= int(number[2]):
		first3 = True

	if int(num[3]) > int(num[4]) and int(num[4]) > int(num[5]):
		last3 = True

	if first3 == True and last3 == True:
		return True
	else:
		return False

numbers_str = parse_file()

counter = 0

for num in numbers_str:
	if check_num(num) == True:
		counter += 1

print(counter)