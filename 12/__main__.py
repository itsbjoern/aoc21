import util
from collections import defaultdict

init = util.get_input(12)

uni = defaultdict(lambda: {})
bi = defaultdict(lambda: {})
for line in init:
  [fr, to] = line.split('-')
  uni[fr][to] = to.isupper()
  bi[fr][to] = to.isupper()
  bi[to][fr] = fr.isupper()

def search(paths, allow_double=False):
  found = []
  for key, upper in bi[paths[-1][-1]].items():
    cnt = paths[-1].count(key)
    double = allow_double
    if not upper:
      if double and key not in ['start', 'end']:
        if cnt == 1:
          double = False
        elif cnt > 1:
          continue
      elif cnt > 0:
        continue

    path = paths[-1] + [key]
    if path in paths:
      continue
    if key == 'end':
      found.append(path)
      continue
    found += search(paths + [path], allow_double=double)
  return found

paths = search([['start']])
print(len(paths))

paths = search([['start']], allow_double=True)
print(len(paths))
