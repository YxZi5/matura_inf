#!/usr/bin/python3


def czy_mniejszy(n, s, k1, k2):
	i = int(k1)
	j = int(k2)

	n = int(n)

	while i <= n and j <= n:
		if s[i] == s[j]:
			i = i + 1
			j = j + 1
		else:
			if s[i] < s[j]:
				return True
			else:
				return False
	if j <= n:
		return True
	else:
		return False


for i in range(1, 4):
	path = f"DANE/DANE_M/slowa{i}.txt"
	with open(path, "r") as slowa:
		lines = slowa.read().splitlines()
		n = lines[0]
		s = lines[1]
		k1 = lines[2].split(' ')[0]
		k2 = lines[2].split(' ')[1].split(' ')[0]

		out = czy_mniejszy(n, s, k1, k2)

		print(f"slowa{i}.txt => {out}")
		# print(path)
		# if out == "True":
		# 	print(f"{path} - TAK")
		# else:
		# 	print(f"{path} - NIE")

# with open("DANE/DANE_M/slowa1.txt", "r") as slowa:
# 	lines = slowa.read().splitlines()
# 	n = int(lines[0])
# 	s = lines[1]
# 	k1 = int(lines[2].split(' ')[0])
# 	k2 = int(lines[2].split(' ')[1].split(' ')[0])
# 	# print(f"{n}, {s}, {k1}, {k2}")
# 	print(czy_mniejszy(n, s, k1, k2))
