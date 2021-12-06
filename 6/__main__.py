init = [int(x) for x in open('6/input.txt').read().split(',')]


def get_fish(init_timers, days):
    day = 0
    timers = {i: init_timers.count(i) for i in range(10)}

    while day < days:
        m = min([k for k, t in timers.items() if t != 0])
        day += m + 1
        cnt_m = timers[m]
        timers = {i: timers[min(i + m + 1, 9)] for i in range(10)}
        timers[8] = cnt_m
        timers[6] += cnt_m

    return sum(timers.values())

print(get_fish(init, 80))
print(get_fish(init, 256))
