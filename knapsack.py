#!/usr/bin/python

import sys
from collections import namedtuple

item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
  cache = [[0]*(capacity+1) for _ in range(len(items)+1)]

  bag = set()

  for range in range(1,len(cache)):
    for size in range(len(cache[item])):

      if items[item-1].size>size:
        cache[item][size] =cache[item-1][size]
      else:

        r1 = cache[item-1][size]
        r2 = cache[item-1][size - items[item-1].size] + items[item-1].value
        cache[item][size] = max(r1,r2)

  rows = len(cache)-1
  cols = len(cache[0]) - 1

  while rows > 0 and cols > 0:
    if cache[rows][cols] != cache[rows-1][cols]:
      bag.add(rows-1)
      rows -= 1
      cols -= items[rows].size
    else:
      rows -= 1

  return cache[-1][-1], bag


if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')