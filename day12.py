import re
import numpy as np

test_str = """
initial state: #..#.#..##......###...###

...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #
"""

with open('day12.txt') as fp:
    rows = fp.readlines()

init_str = re.match(r'initial state: ([#\.]+)', rows[0]).group(1)
init_state = np.array([1 if c == '#' else 0 for c in init_str])

regex = re.compile(r'([#\.]{5}) => ([#\.])')
rules = []
results = []

for row in rows[2:]:
    m = regex.match(row)
    assert m is not None
    rules.append([1 if c == '#' else 0 for c in m.group(1)])
    results.append(1 if m.group(2) == '#' else 0)

rules = np.array(rules)
results = np.array(results)

def part1():
    left_idx = -30
    right_idx = len(init_state) + 30
    state = np.zeros(right_idx - left_idx, dtype=int)
    state[-left_idx:len(init_state)-left_idx] = init_state
    print(state)

    for n in range(20):
        if n % 100 == 0:
            print('{} of {} done'.format(n, 50000000000))

        next_state = state.copy()

        for i in range(2, len(state) - 2):
            for rule, result in zip(rules, results):
                if np.array_equal(state[i-2:i+3], rule):
                    next_state[i] = result
                    break

        if np.array_equal(state, next_state):
            print(n)
            break

        state = next_state

    print(state)
    idx = np.arange(left_idx, right_idx)
    print(idx)
    return np.sum(state * idx)


print(part1())

