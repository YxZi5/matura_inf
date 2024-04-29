#!/usr/bin/python3

def load_numbers():
	numbers = []
	with open("dane/pierwsze.txt", "r") as liczby:
		liczby = liczby.read().splitlines()
		for liczba in liczby:
			numbers.append(liczba)
	return numbers

def main(num):
	liczba_dwa = 0
	pointer = 0
	for znak in range(len(str(num))):
		liczba_dwa += int(num[znak])

	return liczba_dwa

if __name__ == '__main__':
	liczby = load_numbers()
	pointer = 0
	liczby_dwa = []
	liczby_trzy = []
	liczby_cztery = []
	for i in range(len(liczby)):
		number_two = main(liczby[i])
		if number_two == 1:
			pointer += 1
		if len(str(number_two)) > 1:
			liczby_dwa.append(number_two)

	for k in range(len(liczby_dwa)):
		number_tree = main(str(liczby_dwa[k]))
		if number_tree == 1:
			pointer += 1
		if len(str(number_tree)) > 1:
			liczby_trzy.append(number_tree)

	for j in range(len(liczby_trzy)):
		num_four = main(str(liczby_trzy[j]))
		if num_four == 1:
			pointer += 1
		if len(str(num_four)) > 1:
			liczby_cztery.append(num_four)

	print(f"{pointer} Liczb")