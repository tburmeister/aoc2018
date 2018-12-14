import numpy as np


def part1(n_recipes=598701):
    recipes = np.zeros(n_recipes + 11, dtype=int)
    recipes[0:2] = [3, 7]
    idx1 = 0
    idx2 = 1
    n = 2

    while n < n_recipes + 10:
        new = recipes[idx1] + recipes[idx2]
        if new >= 10:
            recipes[n:n+2] = [1, new % 10]
            n += 2
        else:
            recipes[n] = new
            n += 1

        idx1 = (idx1 + 1 + recipes[idx1]) % n
        idx2 = (idx2 + 1 + recipes[idx2]) % n

    return recipes[n_recipes:n_recipes+10]


def part2():
    seq = [5, 9, 8, 7, 0, 1]
    # seq = [5, 9, 4, 1, 4]
    recipes = np.zeros(100000, dtype=int)
    capacity = 100000
    recipes[0:2] = [3, 7]
    idx1 = 0
    idx2 = 1
    n = 2
    m = len(seq)

    while True:
        if n > capacity - 2:
            capacity *= 10
            new_recipes = np.zeros(capacity, dtype=int)
            new_recipes[:n+1] = recipes
            recipes = new_recipes

        new = recipes[idx1] + recipes[idx2]
        if new >= 10:
            recipes[n:n+2] = [1, new % 10]
            n += 2
        else:
            recipes[n] = new
            n += 1

        idx1 = (idx1 + 1 + recipes[idx1]) % n
        idx2 = (idx2 + 1 + recipes[idx2]) % n

        if np.array_equal(recipes[n-m:n], seq):
            return n - m
        elif np.array_equal(recipes[n-m-1:n-1], seq):
            return n - m - 1


# print(''.join(map(str, part1())))
print(part2())

