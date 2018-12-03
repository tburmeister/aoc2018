import re

from collections import Counter

regex = re.compile(r'#\d+ @ (\d+),(\d+): (\d+)x(\d+)')

with open('day3.txt') as fp:
    rows = fp.readlines()


def part1():
    covered = Counter()
    out = 0

    for row in rows:
        m = regex.match(row)
        assert m is not None
        x0 = int(m.group(1))
        y0 = int(m.group(2))
        x1 = x0 + int(m.group(3))
        y1 = y0 + int(m.group(4))

        for i in range(x0, x1):
            for j in range(y0, y1):
                covered[(i, j)] += 1

    for count in covered.values():
        if count > 1:
            out += 1

    return out


def part2():
    covered = Counter()
    cuts = []

    for row in rows:
        m = regex.match(row)
        assert m is not None
        x0 = int(m.group(1))
        y0 = int(m.group(2))
        x1 = x0 + int(m.group(3))
        y1 = y0 + int(m.group(4))
        cuts.append((x0, y0, x1, y1))

        for i in range(x0, x1):
            for j in range(y0, y1):
                covered[(i, j)] += 1

    for idx, (x0, y0, x1, y1) in enumerate(cuts):
        okay = True
        for i in range(x0, x1):
            for j in range(y0, y1):
                if covered[(i, j)] > 1:
                    okay = False
                    break

            if not okay:
                break

        if okay:
            return idx + 1


if __name__ == '__main__':
    print(part2())
