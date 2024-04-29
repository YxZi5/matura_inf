#!/usr/bin/python3

with open("../Dane_2305/pi.txt") as pi:
  pi = pi.read().splitlines()
  
dataset = {}

dataset['00'] = 0

for i in range(0, len(pi)):
  
  if i == len(pi)-1:
    break
  
  current_number = f"{pi[i]}{pi[i+1]}"
  
  if current_number in dataset:
    dataset[current_number] += 1
  else:
    dataset[current_number] = 1

dataset_values = list(dataset.values())
min_value = min(dataset_values)
max_value = max(dataset_values)

for key, value in dataset.items():
  
  if value == min_value:
    print(f"MIN VALUE: {key} {value}")
  
  if value == max_value:
    print(f"MAX VALUE: {key} {value}")