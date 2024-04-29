#!/usr/bin/python3

# def iloczyn(x, y):
# 	if y == 1:
# 		return x
# 	else:
# 		k = int(y / 2)
#
# 		print(f"wywolanie: iloczyn({x}, {k})")
#
# 		z = iloczyn(x, k)
#
# 		if y % 2 == 0:
# 			print(f"operacja: {z} + {z}")
# 			print(f"k: {k}\nz:{z}")
# 			return z + z
# 		else:
# 			print(f"operacja: {x} + {z} + {z}")
# 			print(f"k: {k}\nz:{z}")
# 			return x + z + z

liczba_dodawan = 0

def iloczyn2(x, y):
	global liczba_dodawan

	if y == 1:
		return x
	else:
		k = int(y / 2)
		z = iloczyn2(x, k)

		if y % 2 == 0:
			liczba_dodawan += 1
			return z + z
		else:
			liczba_dodawan += 2
			return x + z + z

print(iloczyn2(112, 112))

print(f"liczba dodawan: {liczba_dodawan}")