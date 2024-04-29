#!/usr/bin/python3

# to jest teoretycznie źle tzn funkcja wyciagajaca sufyxy jest git
# ale zadanie jest źle i chhuj wie o co w nim wsm chodzi, ale to
# tutaj zostawiam niech sobie bedzie.

def parse_sufiks(word):
	sufiksy = []
	reversed_word = word[::-1]
	sufiks = ""
	sufiksy.append(word)
	for k in range(1, len(word)+1):
		for i in range(0, len(reversed_word)-k):
			sufiks += reversed_word[i]
		sufiksy.append(sufiks[::-1])
		sufiks = ""
	sufiksy.pop()

	return sufiksy[::-1]

# with open("DANE/DANE_M/sufiks_4.txt", "r") as linie:
# 	linie = linie.read().splitlines()
# 	for line in linie:
# 		s = line.split(" ")[1]
	
# 		ss = parse_sufiks(s)
# 		x = []

# 		for sufix in ss:
# 			if sufix[0] == "a":
# 				x.append(sufix)

# 		print(x[0])

ss = parse_sufiks("maturazinformatyki")

for j in ss:
	if j[0] == "a":
		print(j)