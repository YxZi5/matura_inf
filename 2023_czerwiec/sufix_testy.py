#!/usr/bin/python3

slowo = "mascarpone"

def get_sufixes(word):
  tab = []
  
  for k in range(1, len(word)):
    sufix = ""
    
    for i in range(k, len(word)):
      sufix += word[i]
    
    tab.append(sufix)
  
  return tab

with open("DANE/DANE_M/slowa4.txt", "r") as sufixy:
  sufixy = sufixy.read().splitlines()
  
for line in sufixy:
  line = line.split()
  s = line[1]
  
  word_sufixes = get_sufixes(s)
  sorted_sufiex = sorted(word_sufixes)
  
  print(f"{sorted_sufiex[0]}")
