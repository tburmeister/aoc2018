from collections import Counter

with open('day2.txt') as fp:
    box_ids = fp.read().splitlines()


def part1():
    twice = 0
    thrice = 0

    for box_id in box_ids:
        counts = Counter()
        for char in box_id:
            counts[char] += 1

        for count in counts.values():
            if count == 2:
                twice += 1
                break

        for count in counts.values():
            if count == 3:
                thrice += 1
                break

    return twice * thrice


def part2():
    for i in range(len(box_ids)):
        for j in range(i + 1, len(box_ids)):
            diff = 0
            for char1, char2 in zip(box_ids[i], box_ids[j]):
                if char1 != char2:
                    diff += 1

            if diff == 1:
                return box_ids[i], box_ids[j]


print(part1())
print(part2())

