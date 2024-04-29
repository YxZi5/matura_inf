#!/usr/bin/python3

def obl_opis(ciag):
	L = 1
	for i in range(0, len(ciag)-1):
		if ciag[i] != ciag[i+1]:
			L += 1
	return L*2

if __name__ == '__main__':
	c = [1, 1, 3, 2, 2, 2, 1]
	c2 = [2, 2, 2, 2, 2, 6]
	print(obl_opis(c2))