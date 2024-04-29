#!/usr/bin/python3

def algorytm(k):
	A = [0]
	for i in range(1, k+1):
		A.append(i)

	s = A[1]

	for i in range(1, k+1):
		p = 0
		for j in range(i, k+1):
		
			p += A[j]
		
			if s < p:
				s = p

	return s

print(algorytm(11))