#!/usr/bin/python3

# NIE DZIALA ZWRACA ZLY WYNIK

import csv

def parse_date(data):
  output_data = ""
  
  for i in range(0, len(data)):
    if data[i] == "-":
      continue
    else:
      output_data += data[i]
  
  return output_data

with open("../Dane_2212/pokoje.txt", "r") as pokoje:
  pokoje = csv.reader(pokoje, delimiter="\t")
  next(pokoje)
  
  pokoje_N = []
  
  for row in pokoje:
    standard = row[1]
    
    if standard == "N":
      pokoje_N.append(row)
      
with open("../Dane_2212/noclegi.txt", "r") as noclegi:
  noclegi = csv.reader(noclegi, delimiter="\t")
  next(noclegi)
  
  noclegi_dane = []
  
  for row in noclegi:
    nr_pokoju = row[4]
    nr_dowodu = row[3]
    
    elem = [nr_pokoju, nr_dowodu]
    noclegi_dane.append(elem)
  
with open("../Dane_2212/klienci.txt", "r") as klienci:
  klienci = csv.reader(klienci, delimiter="\t")
  next(klienci)
  
  klienci_dane = []
  
  for row in klienci:
    miejscowosc = row[3]
    nr_dowodu = row[2]
    
    if miejscowosc == "Opole" and miejscowosc == "Katowice":
      klienci_dane.append(nr_dowodu)

wynajmowali_opoleKatowice = []

for row in noclegi_dane:
  dowod = row[1]
  pokoj = row[0]
  
  if dowod in klienci_dane:
    wynajmowali_opoleKatowice.append(pokoj)

nieZopolaKatowic = []

for row in pokoje_N:
  nr = row[0]
  
  if nr not in wynajmowali_opoleKatowice:
    nieZopolaKatowic.append(nr)

for i in range(0, len(nieZopolaKatowic)):
  print(nieZopolaKatowic[i])

