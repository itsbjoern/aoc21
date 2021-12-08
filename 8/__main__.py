from os import stat
import util

init = util.get_input(8)

static = {
  'abcefg': 0,
  'cf': 1,
  'acdeg': 2,
  'acdfg': 3,
  'bcdf': 4,
  'abdfg': 5,
  'abdefg': 6,
  'acf': 7,
  'abcdefg': 8,
  'abcdfg': 9
}

def get_mapping(mapping):
  curr_origins = [set(x) for x in mapping.split()]

  nmap = {}
  known_mappings = {}

  left_origins = []
  for origin in curr_origins:
    if len(origin) == 2:
      nmap[1] = origin
    elif len(origin) == 3:
      nmap[7] = origin
    elif len(origin) == 4:
      nmap[4] = origin
    elif len(origin) == 7:
      nmap[8] = origin
    else:
      left_origins.append(origin)
  curr_origins = left_origins
  left_origins = []

  for origin in curr_origins:
    if len(origin) == 5:
      diff7 = origin.difference(nmap[7])
      if len(diff7) == 2:
        nmap[3] = origin
        continue
      else:
        len_diff74 = len(diff7.difference(nmap[4]))
        if len_diff74 == 2:
          nmap[2] = origin
          continue
        elif len_diff74 == 1:
          nmap[5] = origin
          continue
    left_origins.append(origin)
  curr_origins = left_origins
  left_origins = []

  known_mappings['a'] = nmap[7].difference(nmap[1]).pop()
  known_mappings['b'] = nmap[5].difference(nmap[3]).pop()
  known_mappings['c'] = nmap[2].intersection(nmap[1]).pop()
  known_mappings['d'] = nmap[3].intersection(nmap[4]).difference(nmap[1]).pop()
  known_mappings['e'] = nmap[2].difference(nmap[3]).pop()
  known_mappings['f'] = nmap[5].intersection(nmap[1]).pop()
  known_mappings['g'] = nmap[3].difference(nmap[4]).difference(nmap[7]).pop()

  final_mapping = {}
  for static_num, value in static.items():
    mapped = ''.join(sorted([known_mappings[key] for key in static_num]))
    final_mapping[mapped] = value

  return final_mapping

result_1 = {}
result_2 = 0
for line in init:
  split = line.split(' | ')
  mmap = get_mapping(split[0])

  display = split[1].split()
  number = ''
  for num in display:
    resolved = mmap[''.join(sorted(num))]
    number += str(resolved)
    result_1.setdefault(resolved, 0)
    result_1[resolved] += 1
  result_2 += int(number)

print(sum([
  result_1[1],
  result_1[4],
  result_1[7],
  result_1[8],
]))

print(result_2)