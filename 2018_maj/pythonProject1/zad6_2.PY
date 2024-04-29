#!/usr/bin/python3

import csv

with open("../DANE/komputery.txt", "r") as komputery:
  komputery = csv.reader(komputery, delimiter="\t")
  next(komputery)
  
  komputery_A = []
  
  for row in komputery:
    sekcja = row[1]
    if sekcja == "A":
      komputery_A.append(row)

with open("../DANE/awarie.txt", "r") as awarie:
  awarie = csv.reader(awarie, delimiter="\t")
  next(awarie)
  
  awarie_komputery_A = []
  
  for row in awarie:
    num_komp = row[1]
    
    for row2 in komputery_A:
      num = row2[0]
      
      if num == num_komp:
        awarie_komputery_A.append(row)

with open("../DANE/naprawy.txt", "r") as naprawy:
  naprawy = csv.reader(naprawy, delimiter="\t")
  next(naprawy)
  
  # id_zgloszenia | id_komputera | rodzaj_naprawy
  naprawy_komputery_A = []
  
  for row in naprawy:
    zgloszenie = row[0]
    rodzaj = row[2]
    rodzaj = row[2]
    
    
    for row2 in awarie_komputery_A:
      zgloszenie_nr = row2[0]
      komputer_nr = row2[1]
      
      if zgloszenie == zgloszenie_nr and rodzaj == "wymiana":
        elem = [zgloszenie_nr, komputer_nr, rodzaj]
        naprawy_komputery_A.append(elem)

naprawy_dataset = {}

for row in naprawy_komputery_A:
  id_komputera = row[1]
  
  if id_komputera in naprawy_dataset:
    naprawy_dataset[id_komputera] += 1
  else:
    naprawy_dataset[id_komputera] = 1

for key, value in naprawy_dataset.items():
  
  if value >= 10:
    print(f"Numer komputera: {key} liczba wymian: {value}")