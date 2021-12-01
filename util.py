import os

def get_input(num):
  with open(f'{num}/input.txt') as fh:
    return fh.read().split('\n')

def get_nums(num):
  return [float(x) for x in get_input(num)]
