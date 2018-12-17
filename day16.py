import re

re_before = re.compile(r'Before: \[(\d+), (\d+), (\d+), (\d+)\]')
re_inst = re.compile(r'(\d+) (\d+) (\d+) (\d+)')
re_after = re.compile(r'After:  \[(\d+), (\d+), (\d+), (\d+)\]')


with open('day16.txt') as fp:
    rows = fp.readlines()

examples = []
curr = []
instructions = []

for idx, row in enumerate(rows):
    if idx % 4 == 0:
        m = re_before.match(row)
        if m is None:
            break
        curr.append(list(map(int, m.groups())))
    elif idx % 4 == 1:
        m = re_inst.match(row)
        assert m is not None, row
        curr.append(list(map(int, m.groups())))
    elif idx % 4 == 2:
        m = re_after.match(row)
        assert m is not None, row
        curr.append(list(map(int, m.groups())))
        examples.append(curr)
        curr = []

for row in rows[idx:]:
    m = re_inst.match(row)
    if m is None:
        continue
    instructions.append(list(map(int, m.groups())))


def operation(regs, opcode, a, b):
    ops = [
            ('addr', lambda x, y: regs[x] + regs[y]),
            ('addi', lambda x, y: regs[x] + y),
            ('mulr', lambda x, y: regs[x] * regs[y]),
            ('muli', lambda x, y: regs[x] * y),
            ('banr', lambda x, y: regs[x] & regs[y]),
            ('bani', lambda x, y: regs[x] & y),
            ('borr', lambda x, y: regs[x] | regs[y]),
            ('bori', lambda x, y: regs[x] | y),
            ('setr', lambda x, y: regs[x]),
            ('seti', lambda x, y: x),
            ('gtir', lambda x, y: 1 if x > regs[y] else 0),
            ('gtri', lambda x, y: 1 if regs[x] > y else 0),
            ('gtrr', lambda x, y: 1 if regs[x] > regs[y] else 0),
            ('eqir', lambda x, y: 1 if x == regs[y] else 0),
            ('eqri', lambda x, y: 1 if regs[x] == y else 0),
            ('eqrr', lambda x, y: 1 if regs[x] == regs[y] else 0)
    ]
    return ops[opcode][1](a, b)


def part1():
    count = 0

    for before, (_, a, b, c), after in examples:
        matched = 0
        for i in range(16):
            val = operation(before, i, a, b)
            if val == after[c]:
                matched += 1

        assert matched > 0
        if matched > 2:
            count += 1

    return count


def part2():
    opcodes = [set(range(16)) for i in range(16)]

    for before, (op, a, b, c), after in examples:
        matched = set()
        for i in range(16):
            val = operation(before, i, a, b)
            if val == after[c]:
                matched.add(i)

        opcodes[op].intersection_update(matched)

    for opcode in opcodes:
        print(opcode)

    singletons = set()
    done = False
    while not done:
        done = True
        for opcode in opcodes:
            if len(opcode) == 1:
                singletons = singletons.union(opcode)
            else:
                done = False

        for opcode in opcodes:
            if len(opcode) != 1:
                opcode.difference_update(singletons)

    registers = [0] * 4
    for op, a, b, c in instructions:
        val = operation(registers, list(opcodes[op])[0], a, b)
        registers[c] = val

    print(registers)
    return registers[0]


print(part2())

