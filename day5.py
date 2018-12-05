with open('day5.txt') as fp:
    raw = fp.read().strip()


def part1(b):
    low = 0
    high = 1

    while high < len(b):
        if abs(b[low] - b[high]) == 32:
            b[low] = b[high] = 0

            high += 1
            assert high >= len(b) or b[high] != 0

            while b[low] == 0 and low >= 0:
                low -= 1

            if low < 0:
                low = high
                high += 1

        else:
            low = high
            high += 1

    count = 0
    
    for char in b:
        if char > 1:
            count += 1

    return count


# print(part1('dabAcCaCBAcCcaDA'))
# print(part1('eabcCBA'))

b = bytearray(raw.encode())
print(part1(b))


def part2():
    lowest = len(raw)

    for char in range(65, 97):
        b = bytearray(raw.encode())
        c = bytearray()

        for i in range(len(b)):
            if b[i] != char and b[i] != char + 32:
                c.append(b[i])

        count = part1(c)
        if count < lowest:
            lowest = count

    return lowest


print(part2())

