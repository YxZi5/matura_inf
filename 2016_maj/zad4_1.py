#!/usr/bin/python3

with open('Dane_NOWA/punkty.txt', 'r') as file:
	file = file.read().splitlines()

# with open('test.txt', 'r') as file:
# 	file = file.read().splitlines()

x = 200
y = 200

r = 200

a = []
b = []

krawedz_kola = []

counter = 0

for line in file:
	liczby = line.split()
	a = int(liczby[0])
	b = int(liczby[1])

	# (x - a)^2 + (y - b)^2 = r^2
	output = (((a - x)**2) + ((b - y)**2))

	if output == r**2:
		s = f"({str(a)}, {str(b)})"
		krawedz_kola.append(s)

	if output < r**2:
		counter += 1

print(f"Ilosc nalezanych do okregu: {counter}")
print(f"Punkty znajdujace sie na krawedzi okregu: {krawedz_kola}")