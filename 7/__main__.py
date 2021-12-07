init = [int(x) for x in open('7/input.txt').read().split(',')]

def min_dist(data):
  return min([sum([abs(x - i) for x in init]) for i in range(len(data))])

print(min_dist(init))

def min_dist2(data):
  return min([sum([sum(range(abs(x - i) + 1)) for x in init]) for i in range(len(data))])

print(min_dist2(init))
