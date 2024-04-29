#!/usr/bin/python3

def cyfropodobne(l1, l2):
	l1 = str(l1)
	l2 = str(l2)

	# for first number
	for i in range(0, len(l1)):

		if l1[i] not in l2:
			return False

	# for second num
	for k in range(0, len(l2)):

		if l2[k] not in l1:
			return False

	return True

with open("punkty.txt", "r") as punkty:
	punkty = punkty.read().splitlines()

counter = 0

for linia in punkty:

	tab = linia.split()

	l1 = int(tab[0])
	l2 = int(tab[1])

	if cyfropodobne(l1, l2) == True:
		counter += 1

print(counter)
