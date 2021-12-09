import util

init = util.get_input(9)

cave = []
visited = []
peaks = []
for i, srow in enumerate(init):
  visited.append([False] * len(srow))
  row = []
  for j, s_col in enumerate(srow):
    row.append(int(s_col))
    if s_col == '9':
      peaks.append((j, i))
      visited[i][j] = True
  cave.append(row)

def descend(curr):
  [x, y] = curr

  val = cave[y][x]
  visited[y][x] = True
  coords = []

  if x > 0: coords.append((x - 1, y))
  if x < len(cave[0]) - 1: coords.append((x + 1, y))

  if y > 0: coords.append((x, y - 1))
  if y < len(cave) - 1: coords.append((x, y + 1))

  has_smaller = False
  basins = []
  low_points = []
  for [cx, cy] in coords:
    cval = cave[cy][cx]
    if not visited[cy][cx]:
      loc_low_points, loc_basin = descend((cx, cy))
      low_points += loc_low_points
      if cval != 9:
        loc_basin += [(cx, cy)]
      basins.append(loc_basin)
    if cval <= val:
      has_smaller = True
  if not has_smaller:
    low_points.append(curr)
  if val != 9:
    basins = [c for b in basins for c in b]
  return low_points, basins

lows = []
basins = []
for peak in peaks:
  low_pts, bs = descend(peak)
  lows += low_pts
  basins += [len(b) for b in bs]

lows_points = [cave[y][x] + 1 for [x, y] in lows]
print(sum(lows_points))

basin_result = 1
for bsize in sorted(basins)[-3:]:
  basin_result *= bsize
print(basin_result)
