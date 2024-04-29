#!/usr/bin/python3

with open("dane/liczby.txt", "r") as numbers:
	numbers = numbers.read().splitlines()

counter_przez2 = 0
counter_przez8 = 0

for i in range(0, len(numbers)):
	dec_num = int(str(numbers[i]), 2)

	if dec_num % 2 == 0:
		counter_przez2 += 1

	if dec_num % 8 == 0:
		counter_przez8 += 1

print(f"ilosc podzielnych przez 2: {counter_przez2}\nilosc podzielnych przez 8: {counter_przez8}")