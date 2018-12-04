import re

from collections import Counter

with open('day4.txt') as fp:
    rows = fp.readlines()
    rows.sort()

r1 = re.compile(r'\[\d\d\d\d-\d\d-\d\d \d\d:\d\d\] Guard #(\d+) begins shift')
r2 = re.compile(r'\[\d\d\d\d-\d\d-\d\d 00:(\d\d)\] falls asleep')
r3 = re.compile(r'\[\d\d\d\d-\d\d-\d\d 00:(\d\d)\] wakes up')


def part1():
    guards = {}
    print(rows)

    for i in range(0, len(rows), 3):
        m1 = r1.match(rows[i])
        assert m1 is not None, rows[i]
        m2 = r2.match(rows[i + 1])
        assert m2 is not None
        m3 = r3.match(rows[i + 2])
        assert m3 is not None

        guard = int(m1.group(1))
        asleep = int(m2.group(1))
        awake = int(m3.group(1))

        if guard not in guards:
            guards[guard] = [0, Counter()]

        guards[guard][0] += awake - asleep
        for j in range(asleep, awake):
            guards[guard][1][j] += 1

    high_total = 0
    high_guard = 0
    high_minutes = None

    for guard, (total, minutes) in guards.items():
        if total > high_total:
            high_total = total
            high_guard = guard
            high_minutes = minutes

    high_count = 0
    high_minute = 0

    for minute, count in minutes.items():
        if count > high_count:
            high_count = count
            high_minute = minute

    return high_guard * high_minute


print(part1())
