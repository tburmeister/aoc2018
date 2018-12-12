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
    left_idx = -5
    right_idx = len(init_state) + 5
    state = np.zeros(right_idx - left_idx, dtype=int)
    state[-left_idx:len(init_state)-left_idx] = init_state
    print(state)
    start_left = 0
    clip_left = 0
    start_right = 0
    clip_right = 0

    for n in range(50000000000):
        if n % 100000000 == 0:
            print('{} of {} done'.format(n, 50000000000))

        next_state = np.zeros(right_idx - left_idx, dtype=int)
        print(left_idx, right_idx)
        print(start_left, clip_left)
        print(start_right, clip_right)
        next_state[start_left:len(next_state) - clip_left - clip_right] = state[clip_left:len(state)-clip_right]

        for i in range(2, len(next_state) - 2):
            for rule, result in zip(rules, results):
                if np.array_equal(state[i-2:i+3], rule):
                    next_state[i] = result
                    break

        if np.array_equal(state, next_state):
            print(n)
            break

        start_left = 0
        clip_left = 0
        if np.sum(next_state[:10]) == 0:
            left_idx += 5
            clip_left = 5
        elif np.sum(next_state[:5]) > 0:
            left_idx -= 5
            start_left = 5

        start_right = 0
        clip_right = 0
        if np.sum(next_state[-10:]) == 0:
            right_idx -= 5
            clip_right = 5
        elif np.sum(next_state[-5:]) > 0:
            right_idx += 5
            start_right = 5

        state = next_state

    print(state)
    idx = np.arange(left_idx, right_idx)
    print(idx)
    return np.sum(state * idx)


print(part1())

