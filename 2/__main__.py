import util

lines = util.get_input(2)
x = 0
y = 0
z = 0

for line in lines:
    [direction, dist] = line.split(' ')
    dist = int(dist)
    if direction == 'forward':
        x += dist
        z += y * dist
    elif direction == 'up':
        y -= dist
    else:
        y += dist

print(x * y)
print(z * x)