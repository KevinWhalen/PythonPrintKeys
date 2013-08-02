#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Use as:
# from printKeys import printKeys

# Basically a depth first search that prints ".keys()" for objects mixed 
# with dictionaries, lists, integers, longs, floats, or strings. 
def printKeys(mixed_object, spacing = 0):
  tab = ""
  for i in range(spacing):
    tab += " "
  for k in mixed_object: #sorted(mixed_object, key=mixed_object.get):
    if type(mixed_object[k]) == dict:
      print tab + k
      printKeys(mixed_object[k], spacing + 2)
    elif type(mixed_object[k]) == list:
      for l in range(len(mixed_object[k])):
        print tab + k
        printKeys(mixed_object[k][l], spacing + 2)
    elif type(mixed_object[k]) in [int, long, float]:
      print tab + str(k)
    else:
      print tab + k
