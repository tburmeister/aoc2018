import sys

with open('day8.txt') as fp:
    raw = list(map(int, fp.read().strip().split()))


class Node:
    def __init__(self):
        self.children = []
        self.meta = []


def parse(data, idx):
    node = Node()
    n = data[idx]
    m = data[idx+1]
    idx += 2

    for i in range(n):
        idx, child = parse(data, idx)
        node.children.append(child)

    for i in range(m):
        node.meta.append(data[idx+i])

    return idx + m, node


def walk(root, n):
    for child in root.children:
        n = walk(child, n)

    return n + sum(root.meta)


def part1():
    idx, root = parse(raw, 0)
    assert idx == len(raw), '{} != {}'.format(idx, len(raw))
    return walk(root, 0)


def walk2(root, n):
    if len(root.children) == 0:
        return n + sum(root.meta)

    for i in root.meta:
        if i - 1 < len(root.children):
            n = walk2(root.children[i-1], n)

    return n


def part2():
    idx, root = parse(raw, 0)
    return walk2(root, 0)


print(part2())

