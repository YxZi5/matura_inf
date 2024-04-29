#!/usr/bin/python3

with open("DANE/dane.txt", "r") as pixele:
	pixele = pixele.read().split()

all_pixele = []

for elem in pixele:
	all_pixele.append(int(elem))

all_pixele = sorted(all_pixele)

naj = all_pixele[len(all_pixele)-1]
najlow = all_pixele[0]

print(f"najjasniejszy: {naj}")
print(f"najciemniejszy: {najlow}")