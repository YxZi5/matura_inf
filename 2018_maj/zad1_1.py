#!/usr/bin/python3

def algorytm(n):
	p = 1
	q = n

	while p < q:
		s = int((p+q) / 2)

		if s*s*s < n:
			p = s + 1
		else:
			q = s

	return p

# 1.2:
for i in range(100, 1100):

	if algorytm(i) != 10:
		continue

	print(i)
