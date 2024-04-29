#!/usr/bin/python3

import csv

# example input
# [['365', '8'], ['249', '3'], ['312', '4'], ['275', '5'], ['379', '7']
# '249'
def get_priorytety(tab, komp_nr):
  
  return_tab = []
  
  for row in tab:
    komputer_nr = row[0]
    prio = row[1]
    
    if komp_nr == komputer_nr:
      prio = int(prio)
      return_tab.append(prio)
  
  return return_tab

with open("../DANE/komputery.txt", "r") as komputery:
  komputery = csv.reader(komputery, delimiter="\t")
  next(komputery)
  
  komputery_dane = []
  
  for row in komputery:
    komputery_dane.append(row)

with open("../DANE/awarie.txt", "r") as awarie:
  awarie = csv.reader(awarie, delimiter="\t")
  next(awarie)
  
  awarie_dane = []
  
  for row in awarie:
    nr_komputera = row[1]
    priorytet = row[3]
    
    elem = [nr_komputera, priorytet]
    
    awarie_dane.append(elem)

komputery_awaryjne_ogolnie = []

for elem in awarie_dane:
  nr = elem[0]
  
  if nr in komputery_awaryjne_ogolnie:
    continue
  else:
    komputery_awaryjne_ogolnie.append(nr)

bezawaryjne = []

for row in komputery_dane:
  nr_komputera = row[0]

  if nr_komputera not in komputery_awaryjne_ogolnie:
    bezawaryjne.append(nr_komputera)
  else:
    priotytety = get_priorytety(awarie_dane, nr_komputera)
    l_prios = len(priotytety)
    
    counter = 0
    
    for p in priotytety:
      if p < 8:
        counter += 1
      else:
        break
    
    if counter == l_prios:
      # print(f"komputer: {nr_komputera} => {priotytety}")
      bezawaryjne.append(nr_komputera)

print(len(bezawaryjne))