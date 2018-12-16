import numpy as np
import time

with open('day15.txt') as fp:
    rows = fp.readlines()

rows1 = """
#######
#.G...#
#...EG#
#.#.#G#
#..G#E#
#.....#
#######""".strip().split('\n')

rows2 = """
#######
#G..#E#
#E#E.E#
#G.##.#
#...#E#
#...E.#
#######""".strip().split('\n')

rows3 = """
#######
#.E...#
#.....#
#...G.#
#######""".strip().split('\n')

rows4 = """
#######
#E..EG#
#.#G.E#
#E.##E#
#G..#.#
#..E#.#
#######""".strip().split('\n')

rows5 = """
#######
#.E...#
#.#..G#
#.###.#
#E#G#G#
#...#G#
#######""".strip().split('\n')

rows = rows

dim_y = len(rows)
dim_x = len(rows[0].strip())

space = np.zeros((dim_y, dim_x), dtype=np.dtype('b'))

for y, row in enumerate(rows):
    for x, char in enumerate(row.strip().encode()):
        space[y][x] = char

class Unit:

    def __init__(self, x, y, board, units, allies, enemies):
        self.x = x
        self.y = y
        self.hp = 200
        self.ap = 3
        self.board = board
        self.units = units
        self.allies = allies
        self.enemies = enemies
        units.append(self)
        allies.append(self)

    def kill(self):
        self.board[self.y][self.x] = b'.'[0]
        self.units.remove(self)
        self.allies.remove(self)

    def attack(self, x, y):
        for unit in self.units:
            if unit.x == x and unit.y == y:
                break

        assert unit is not None
        unit.hp -= self.ap

        if unit.hp <= 0:
            unit.kill()

    def can_attack(self, x, y):
        if self.board[y-1][x] == self.enemy:
            return True, x, y-1
        if self.board[y][x-1] == self.enemy:
            return True, x-1, y
        if self.board[y][x+1] == self.enemy:
            return True, x+1, y
        if self.board[y+1][x] == self.enemy:
            return True, x, y+1

        return False, -1, -1

    def select_attack(self):
        min_hp = 300
        min_x = -1
        min_y = -1

        for unit in self.enemies:
            if abs(unit.x - self.x) + abs(unit.y - self.y) == 1:
                if unit.hp < min_hp:
                    min_hp = unit.hp
                    min_x = unit.x
                    min_y = unit.y

        return min_x, min_y

    def move(self):
        assert self.board[self.y][self.x] == self.ally, \
                'Expected {}, got {}'.format(self.ally, self.board[self.y][self.x])
        visited = np.zeros(self.board.shape, dtype=int) - 1
        d, x, y = self.visit(visited, self.x, self.y)
        if d >= 10000:
            return

        if self.x != x or self.y != y:
            assert self.board[y][x] == b'.'[0]

        self.board[self.y][self.x] = b'.'[0]
        self.x = x
        self.y = y
        self.board[y][x] = self.ally

        if d <= 1:
            xx, yy = self.select_attack()
            self.attack(xx, yy)

        if self.hp <= 0:
            self.board[y][x] = b'.'[0]

    def visit(self, visited, x, y):
        if visited[y][x] >= 0:
            return visited[y][x], x, y

        can, _, _ = self.can_attack(x, y)
        if can:
            visited[y][x] = 0
            return 0, x, y

        # Sentinel
        visited[y][x] = 10000

        to_adjust = []
        mind = 10000
        minx = -1
        miny = -1

        if self.board[y-1][x] == b'.'[0]:
            mind, _, _ = self.visit(visited, x, y-1)
            minx = x
            miny = y-1
            if mind >= 10000:
                to_adjust.append((x, y-1))
        if self.board[y][x-1] == b'.'[0]:
            d, _, _ = self.visit(visited, x-1, y)
            if d < mind:
                mind = d
                minx = x-1
                miny = y
            if mind >= 10000:
                to_adjust.append((x-1, y))
        if self.board[y][x+1] == b'.'[0]:
            d, _, _ = self.visit(visited, x+1, y)
            if d < mind:
                mind = d
                minx = x+1
                miny = y
            if mind >= 10000:
                to_adjust.append((x+1, y))
        if self.board[y+1][x] == b'.'[0]:
            d, _, _ = self.visit(visited, x, y+1)
            if d < mind:
                mind = d
                minx = x
                miny = y+1
            if mind >= 10000:
                to_adjust.append((x, y+1))

        visited[y][x] = mind + 1
        for xx, yy in to_adjust:
            visited[yy][xx] = mind + 2

        return mind + 1, minx, miny


class Elf(Unit):
    enemy = b'G'[0]
    ally = b'E'[0]


class Goblin(Unit):
    enemy = b'E'[0]
    ally = b'G'[0]


def print_board(board):
    for row in board:
        print(bytes(row).decode())

    print()


def part1():
    board = space.copy()
    elves = []
    goblins = []
    units = []
    turns = 0

    for y, row in enumerate(board):
        for x, char in enumerate(row):
            if char == b'E'[0]:
                Elf(x, y, board, units, elves, goblins)
            elif char == b'G'[0]:
                Goblin(x, y, board, units, goblins, elves)

    print(len(elves))
    print(len(goblins))
    print_board(board)
    while len(elves) > 0 and len(goblins) > 0:
        start_len = len(units)
        for idx, unit in enumerate(sorted(units, key=lambda u: u.y * dim_x + u.x)):
            if unit.hp > 0:
                unit.move()
            if len(elves) == 0 or len(goblins) == 0:
                break

        if idx < start_len - 1:
            print('breaking mid turn')
            break

        turns += 1
        print_board(board)

    print_board(board)
    print('{} turns'.format(turns))
    print('{} hp'.format(sum(map(lambda u: u.hp, units))))
    print([u.hp for u in units])
    return turns * sum(map(lambda u: u.hp, units))


print(part1())

