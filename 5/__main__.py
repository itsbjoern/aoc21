import util

lines = util.get_input(5)

result_simple = {}
result = {}
for line in lines:
    [start, end] = line.split(' -> ')
    start = start.split(',')
    end = end.split(',')
    x1, y1 = int(start[0]), int(start[1])
    x2, y2 = int(end[0]), int(end[1])

    if x1 == x2:
        ystride = 1 if y1 < y2 else - 1
        for y in range(int(y1), int(y2) + ystride, ystride):
            key = f'{x1},{y}'
            result.setdefault(key, 0)
            result[key] += 1
            result_simple.setdefault(key, 0)
            result_simple[key] += 1
    elif y1 == y2:
        xstride = 1 if x1 < x2 else - 1
        for x in range(int(x1), int(x2) + xstride, xstride):
            key = f'{x},{y1}'
            result.setdefault(key, 0)
            result[key] += 1
            result_simple.setdefault(key, 0)
            result_simple[key] += 1
    else:
        ystride = 1 if y1 < y2 else - 1
        xstride = 1 if x1 < x2 else - 1

        r = zip(range(int(x1), int(x2) + xstride, xstride), range(int(y1), int(y2) + ystride, ystride))
        for x, y in r:
            key = f'{x},{y}'
            result.setdefault(key, 0)
            result[key] += 1


print(len([x for x in result_simple.values() if x > 1]))
print(len([x for x in result.values() if x > 1]))
