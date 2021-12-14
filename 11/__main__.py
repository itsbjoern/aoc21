import util

init = util.get_input(11)

cave = []
for i, srow in enumerate(init):
  row = []
  for j, s_col in enumerate(srow):
    row.append(int(s_col))
  cave.append(row)

def pprint(grid):
  for row in grid:
    print(''.join([str(x) for x in row]))
  print()

def step(grid, pt, curr):
  [x, y] = pt

  cnt = 0
  if grid[y][x] == 0:
    cnt += 1
    curr.append(pt)
    n_xs = range(max(0, x - 1), min(len(grid[0]) - 1, x + 1) + 1)
    n_ys = range(max(0, y - 1), min(len(grid) - 1, y + 1) + 1)
    for nx in n_xs:
      for ny in n_ys:
        if [nx, ny] in curr:
          continue

        inc = grid[ny][nx] + 1
        grid[ny][nx] = inc if inc < 10 else 0
        cnt += step(grid, [nx, ny], curr)
  return cnt

def get_charged(grid):
  charged = []
  for y, row in enumerate(grid):
    for x, cell in enumerate(row):
      if cell >= 10:
        charged.append([x, y])
        grid[y][x] = 0
  return charged

part1 = cave[:]
comb = 0
# pprint(part1)
steps = 0
while True:
  part1 = [[p + 1 for p in row] for row in part1]
  charged = get_charged(part1)

  curr = charged[:]
  for c in charged:
    comb += step(part1, c, curr)
  steps += 1

  if steps == 100:
    print(comb)
    running = False

  sync = True
  for row in part1:
    if not sync:
      break
    for cell in row:
      if cell != 0:
        sync = False
        break

  if sync:
    print(steps)
    break
