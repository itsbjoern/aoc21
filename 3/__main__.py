import util

lines = util.get_input(3)

gamma, eps = [int(''.join(x), 2) for x in zip(*["10" if x.count("0") < x.count("1") else "01" for x in zip(*lines)])]
print(gamma * eps)

def red(rec, gt=True, i=0):
    x = ''.join([str(int(b.count("1") >= b.count("0") if gt else b.count("0") > b.count("1"))) for b in zip(*rec)])

    if len(rec) == 1: return int(rec[0], 2)
    return red([line for line in rec if line[i] == x[i]], gt, i+1)
ox, co = red(lines), red(lines, False)
print(ox * co)
