#!/usr/bin/python3

def czy_dobra(numbers):
	trojki=open('./trojki.txt', 'w')

	for i in numbers:
		for j in numbers:
			if j%i>0 or i==j:
				continue
			for k in numbers:
				if i==k or j==k:
					continue
				if k%j==0:
					trojki.write(f'{str(i)} {str(j)} {str(k)}\n')
					goodThreeCount+=1
	trojki.close()	

if __name__ == '__main__':
	with open('Dane_2205/przyklad.txt', 'r') as file:
		linie = file.read().splitlines()

		czy_dobra(linie)