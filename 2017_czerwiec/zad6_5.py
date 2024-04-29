#!/usr/bin/python3
import csv

pakiety = open("pakiety.txt", "r")
pakiety = csv.reader(pakiety, delimiter="	")
next(pakiety)

id_pakietow = []

for row in pakiety:
	id_pakietow.append(row[0])

zestawy = open("zestawy.txt", "r")
zestawy = csv.reader(zestawy, delimiter="	")
next(zestawy)
