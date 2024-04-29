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

ile1000 = 0
ile5000 = 0
ile_ogolnie = 0

for i in range(0, 1000):
	liczby = file[i].split()

	a = int(liczby[0])
	b = int(liczby[1])

	# (x - a)^2 + (y - b)^2 = r^2
	output = (((a - x)**2) + ((b - y)**2))

	if output <= r**2:
		ile1000 += 1

for i in range(0, 5000):
	liczby = file[i].split()

	a = int(liczby[0])
	b = int(liczby[1])

	# (x - a)^2 + (y - b)^2 = r^2
	output = (((a - x)**2) + ((b - y)**2))

	if output <= r**2:
		ile5000 += 1

for line in file:
	liczby = line.split()
	a = int(liczby[0])
	b = int(liczby[1])

	# (x - a)^2 + (y - b)^2 = r^2
	output = (((a - x)**2) + ((b - y)**2))

	if output <= r**2:
		ile_ogolnie += 1


i1000 = round((ile1000/1000) * 4, 4)
i5000 = round((ile5000/5000) * 4, 4)
i_all = round((ile_ogolnie/10000) * 4, 4)

print(f"Przybliżona wartosc PI (dla pierwszych 1000 punktow): {i1000}")
print(f"Przybliżona wartosc PI (dla pierwszych 5000 punktow): {i5000}")
print(f"Przybliżona wartosc PI (dla wszystkich punktow) {i_all}")