import util

init = util.get_input(10)

values = {')': 3, ']': 57, '}': 1197, '>': 25137}
order = {k: i + 1 for i, k in enumerate(values.keys())}
match = {'(': ')', '{': '}', '<': '>', '[': ']'}
def step(line, close=''):
  if len(line) == 0:
    return close, False
  if line[0] not in match:
    if line[0] != close[0]:
      return line[0], True
    return step(line[1:], close[1:])
  return step(line[1:], match[line[0]] + close)

faults = {}
scores = []
for line in init:
  f, failed = step(line)
  if failed:
    faults.setdefault(f, 0)
    faults[f] += values.get(f, 0)
  else:
    score = 0
    for c in f:
      score = score * 5 + order[c]
    scores.append(score)
scores = sorted(scores)

print(sum(faults.values()))
print(scores[int(len(scores)/2)])
