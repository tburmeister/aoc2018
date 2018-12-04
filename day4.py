import re

from collections import Counter

with open('day4.txt') as fp:
    rows = fp.readlines()
    rows.sort()

r1 = re.compile(r'\[\d\d\d\d-\d\d-\d\d \d\d:\d\d\] Guard #(\d+) begins shift')
r2 = re.compile(r'\[\d\d\d\d-\d\d-\d\d 00:(\d\d)\] falls asleep')
r3 = re.compile(r'\[\d\d\d\d-\d\d-\d\d 00:(\d\d)\] wakes up')


def guards_info():
    guards = {}
    idx = 0

    while idx < len(rows):
        m1 = r1.match(rows[idx])
        assert m1 is not None, rows[idx]
        idx += 1

        while idx < len(rows):
            m2 = r2.match(rows[idx])
            if m2 is None:
                break

            idx += 1

            m3 = r3.match(rows[idx])
            assert m3 is not None
            idx += 1

            guard = int(m1.group(1))
            asleep = int(m2.group(1))
            awake = int(m3.group(1))

            if guard not in guards:
                guards[guard] = [0, [0] * 59]

            guards[guard][0] += awake - asleep
            for j in range(asleep, awake):
                guards[guard][1][j] += 1

    return guards


def part1():
    guards = guards_info()
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

    for minute, count in enumerate(high_minutes):
        if count > high_count:
            high_count = count
            high_minute = minute

    return high_guard * high_minute


def part2():
    guards = guards_info()
    high_count = 0
    high_guard = 0
    high_minute = 0

    for guard, (_, minutes) in guards.items():
        for minute, count in enumerate(minutes):
            if count > high_count:
                high_count = count
                high_guard = guard
                high_minute = minute

    return high_guard * high_minute


print(part2())

