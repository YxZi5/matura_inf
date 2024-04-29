#!/usr/bin/python3
import math

def oblicz_odleglosc(A, B):
	x1 = int(A[0])
	x2 = int(B[0])

	y1 = int(A[1])
	y2 = int(B[1])

	odeglosc = ((x1 - x2)**2) + ((y1 - y2)**2)
	odeglosc = round(math.sqrt(odeglosc), 0)
	odeglosc = int(odeglosc)

	return odeglosc

with open("punkty.txt", "r") as punkty:
	punkty = punkty.read().splitlines()

najdluzszy = []
naj_odleglosc = 0

for linia in punkty:

	tab = linia.split()
	Xa = tab[0]
	Ya = tab[1]

	for linia_s in punkty:
		tab2 = linia_s.split()
		Xb = tab2[0]
		Yb = tab2[1]

		a = [Xa, Ya]
		b = [Xb, Yb]

		lenght = oblicz_odleglosc(a, b)

		elem = [a, b, lenght]

		if lenght > naj_odleglosc:
			naj_odleglosc = lenght
			najdluzszy = elem
	
print(f"od A({najdluzszy[0][0]}, {najdluzszy[0][1]}) do B({najdluzszy[1][0]}, {najdluzszy[1][1]}) len: {najdluzszy[2]}")
