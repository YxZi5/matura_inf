#!/usr/bin/python3

with open("Dane_2212/mecz.txt", "r") as mecz:
	file = mecz.read().splitlines()

counter = 0

best = ""
passa = ""
for i in range(0, len(file[0])):
	if i == 0:
		if file[0][i] == file[0][i+1]:
			passa += file[0][i]

	acctual_char = file[0][i]
	previous = file[0][i-1]

	if acctual_char != previous:
		if len(passa) >= 9:
			counter += 1
		if len(best) < len(passa):
			best = passa
		passa = ""
	else:
		passa += acctual_char


if "A" in best:
	print(f"{counter} A {len(best)+1}")
	# print(f"Najdłuższą dobrą passę, o długości {len(best)+1}, osiągneła drużyna A")
else:
	print(f"{counter} B {len(best)+1}")
	# print(f"Najdłuższą dobrą passę, o długości {len(best)+1}, osiągneła drużyna B")
