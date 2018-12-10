import re
import numpy as np

np.set_printoptions(threshold=np.nan)
regex = re.compile(r'position=<([ \-]\d+), ([ \-]\d+)> velocity=<([ \-]\d+), ([ \-]\d+)>')

raw_position = []
raw_velocity = []
with open('day10.txt') as fp:
    for row in fp.readlines():
        m = regex.match(row)
        assert m is not None, row
        raw_position.append([int(m.group(1).strip()), int(m.group(2).strip())])
        raw_velocity.append([int(m.group(3).strip()), int(m.group(4).strip())])


def part1():
    position = np.array(raw_position)
    velocity = np.array(raw_velocity)

    metric = 0
    best = None
    seconds = 0
    best_seconds = 0
    while True:
        m = np.max(position[:, 1]) - np.min(position[:, 1])
        if metric == 0 or m < metric:
            metric = m
            best = position.copy()
            best_seconds = seconds

        if m > metric:
            break

        position += velocity
        seconds += 1

    min_x = np.min(best[:, 0])
    max_x = np.max(best[:, 0])
    min_y = np.min(best[:, 1])
    max_y = np.max(best[:, 1])

    print(min_x, max_x, min_y, max_y)
    message = np.zeros((max_y - min_y + 1, max_x - min_x + 1))

    for x, y in best:
        message[y - min_y, x - min_x] = 1

    for row in message:
        for p in row:
            if p == 1:
                print('#', end='')
            else:
                print('.', end='')

        print()

    return best_seconds


print(part1())

