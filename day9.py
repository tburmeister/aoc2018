import re

from collections import deque

regex = re.compile(r'(\d+) players; last marble is worth (\d+) points')

with open('day9.txt') as fp:
    m = regex.match(fp.read())
    players = int(m.group(1))
    final = int(m.group(2))


class Node:

    def __init__(self, value: int):
        self.value = value
        self.next = None
        self.prev = None

    def insert_after(self, value: int):
        new = Node(value)
        new.next = self.next
        new.prev = self
        self.next.prev = new
        self.next = new
        return new

    def pop(self):
        self.next.prev = self.prev
        self.prev.next = self.next
        return self.value, self.next


def part1():
    scores = [0] * players
    start = curr = Node(0)
    curr.next = curr.prev = curr

    for n in range(1, final):
        if n % 10000 == 0:
            print('{} of {}'.format(n, final))

        if n % 23 == 0:
            scores[n % players] += n
            for i in range(7):
                curr = curr.prev

            value, curr = curr.pop()
            scores[n % players] += value
            continue

        curr = curr.next.insert_after(n)

    return max(scores)


final *= 100
print(part1())

