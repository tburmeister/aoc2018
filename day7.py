import re

from collections import Counter

regex = re.compile(r'Step ([A-Z]) must be finished before step ([A-Z]) can begin.')

with open('day7.txt') as fp:
    rows = fp.readlines()


instructions = []
for row in rows:
    m = regex.match(row)
    instructions.append((m.group(1), m.group(2)))


def part1():
    children = {}
    parents = {}

    for a, b in instructions:
        children[a] = []
        children[b] = []
        parents[a] = set()
        parents[b] = set()

    for a, b in instructions:
        children[a].append(b)
        parents[b].add(a)

    out = []
    while len(parents) > 0:
        roots = []
        for node, p in parents.items():
            if len(p) == 0:
                roots.append(node)

        for node in sorted(roots):
            del parents[node]
            out.append(node)
            for child in children[node]:
                parents[child].remove(node)
            break

    return ''.join(out)


def part2():
    children = {}
    parents = {}
    times = Counter()

    for a, b in instructions:
        children[a] = []
        children[b] = []
        parents[a] = set()
        parents[b] = set()

    for a, b in instructions:
        children[a].append(b)
        parents[b].add(a)

    while len(parents) > 0:
        roots = []
        for node, p in parents.items():
            if len(p) == 0:
                roots.append(node)

        for node in sorted(roots):
            times[node] += 61 + ord(node) - ord('A')
            del parents[node]
            for child in children[node]:
                times[child] = max([times[child], times[node]])
                parents[child].remove(node)

    print(times)
    return max(times.values())


print(part2())

