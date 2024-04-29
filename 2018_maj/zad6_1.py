#!/usr/bin/python3
import csv

with open("../DANE/komputery.txt", "r") as komputery:
  komputery = csv.reader(komputery, delimiter="\t")
  next(komputery)
  
  komputery_data = []
  
  for row in komputery:
    komputery_data.append(row)

top_dyski = {}

for elem in komputery_data:
  pojemnosc_dysku = elem[2]
  
  if pojemnosc_dysku in top_dyski:
    top_dyski[pojemnosc_dysku] += 1
  else:
    top_dyski[pojemnosc_dysku] = 1

top_10 = []
for key, value in top_dyski.items():
  top_10.append(value)

top_10 = sorted(top_10)[::-1]

final_values = []
for i in range(0, 10):
  final_values.append(top_10[i])

final_dataset = {}

for i in range(0, len(final_values)):
  
  for key, value in top_dyski.items():
    
    if final_values[i] == value:
      final_dataset[key] = value

for key, value in final_dataset.items():
  print(f"Rodzaj dysku: {key} liczba komputerow: {value}")