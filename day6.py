import numpy as np
# np.set_printoptions(threshold=np.nan)

with open('day6.txt') as fp:
    rows = fp.readlines()
    coords = []
    for row in rows:
        x, y = row.split(', ')
        coords.append((int(x), int(y)))

"""
coords = [
    (1, 1),
    (1, 6),
    (8, 3),
    (3, 4),
    (5, 5),
    (8, 9)
]
"""

min_x, min_y = coords[0]
max_x, max_y = coords[0]

for x, y in coords:
    if x < min_x:
        min_x = x
    if x > max_x:
        max_x = x
    if y < min_y:
        min_y = y
    if y > max_y:
        max_y = y

dim_x = max_x - min_x + 1
dim_y = max_y - min_y + 1


def get_info():
    owned = np.zeros((dim_y, dim_x))
    dist = np.zeros((dim_y, dim_x)) + dim_x + dim_y
    
    for idx, (x, y) in enumerate(coords):
        for i in range(dim_x):
            for j in range(dim_y):
                d = abs((x - min_x) - i) + abs((y - min_y) - j)
                if d < dist[j, i]:
                    dist[j, i] = d
                    owned[j, i] = idx
                elif d == dist[j, i]:
                    owned[j, i] = -1

    return owned, dist


def part1():
    owned, dist = get_info()
    counts = [0] * len(coords)

    for i in range(dim_x):
        for j in range(dim_y):
            idx = int(owned[j, i])
            if idx >= 0:
                counts[idx] += 1

    max_owned = 0
    max_count = 0

    for idx, count in enumerate(counts):
        x, y = coords[idx]
        if float(idx) in owned[0, :] or float(idx) in owned[-1, :] or float(idx) in owned[:, 0] or float(idx) in owned[:, -1]:
            continue
        if count > max_count:
            max_count = count
            max_owned = idx

    return max_owned, max_count


def part2():
    dist = np.zeros((dim_x, dim_y, len(coords)))
    for idx, (x, y) in enumerate(coords):
        for i in range(dim_x):
            for j in range(dim_y):
                d = abs((x - min_x) - i) + abs((y - min_y) - j)
                dist[i, j, idx] = d

    totals = np.sum(dist, 2)
    return len(totals[totals < 10000])

print(part2())

