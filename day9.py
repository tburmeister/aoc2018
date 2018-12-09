import re

from collections import deque

regex = re.compile(r'(\d+) players; last marble is worth (\d+) points')

with open('day9.txt') as fp:
    m = regex.match(fp.read())
    players = int(m.group(1))
    final = int(m.group(2))


def part1():
    scores = [0] * players
    circle = deque()
    circle.append(0)
    idx = 0

    for n in range(1, final):
        if n % 10000 == 0:
            print('{} of {}'.format(n, final))

        if n % 23 == 0:
            scores[n % players] += n
            idx = (idx - 7) % len(circle)
            scores[n % players] += circle[idx]
            del circle[idx]
            continue

        idx = (idx + 2) % len(circle)
        circle.insert(idx, n)

    return max(scores)


final *= 100
print(part1())

