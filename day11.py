import numpy as np


def get_fuel():
    fuel = np.zeros((300, 300))
    x_coords = np.arange(1, 301)
    y_coords = np.arange(1, 301).reshape((300, 1))
    fuel += (x_coords + 10)
    fuel *= y_coords
    fuel += 9810
    fuel *= (x_coords + 10)
    fuel //= 100
    fuel %= 10
    fuel -= 5
    return fuel


def part1():
    fuel = get_fuel()
    high = 0
    x = 0
    y = 0

    for i in range(300 - 3):
        for j in range(300 - 3):
            total = np.sum(fuel[i:i+3, j:j+3])
            if total > high:
                high = total
                x = i
                y = j

    return y + 1, x + 1


def part2():
    fuel = get_fuel()
    high = 0
    size = 0
    x = 0
    y = 0

    for s in range(1, 301):
        for i in range(300 - s):
            for j in range(300 - s):
                total = np.sum(fuel[i:i+s, j:j+s])
                if total > high:
                    high = total
                    size = s
                    x = i
                    y = j

    return y + 1, x + 1, size


print(part2())

