init = open('13/input.txt').read()

[dot_data, fold_data] = init.split('\n\n')

dots = dot_data.split('\n')
folds = fold_data.split('\n')

paper = []
for dot in dots:
  [x, y] = dot.split(',')
  paper.append([int(x), int(y)])


def print_paper(paper):
  visual = ["." * 50] * 10
  for dot in paper:
    visual[dot[1]] = visual[dot[1]][:dot[0]] + '#' + visual[dot[1]][dot[0]+1:]
  for v in visual:
    print(''.join(v))
  print()

for i, fold in enumerate(folds):
  [dir_str, dist_str] = fold.split('=')
  dist = int(dist_str)

  new_dots = []
  for dot in paper:
    new_dot = dot
    if dir_str[-1] == 'x':
      if dot[0] >= dist:
        new_dot = [(dist - dot[0] % dist) % dist, dot[1]]
    else:
      if dot[1] >= dist:
        new_dot = [dot[0], (dist - dot[1] % dist) % dist]
    if new_dot not in new_dots:
      new_dots.append(new_dot)
  paper = new_dots
  if i == 0:
    print(len(paper))

print_paper(paper)
