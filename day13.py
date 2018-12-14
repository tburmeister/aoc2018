import numpy as np

class Cart:

    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.turns = 0

    def intersection(self):
        if self.turns % 3== 0:
            self.turn_left()
        elif self.turns % 3 == 2:
            self.turn_right()

        self.turns += 1

    def turn_left(self):
        if self.dx != 0:
            self.dy = -self.dx
            self.dx = 0
        else:
            self.dx = self.dy
            self.dy = 0

    def turn_right(self):
        if self.dx != 0:
            self.dy = self.dx
            self.dx = 0
        else:
            self.dx = -self.dy
            self.dy = 0


with open('day13.txt') as fp:
    rows = fp.readlines()

dim_y = len(rows)
dim_x = max(map(len, rows))

tracks = np.zeros((dim_y, dim_x), dtype=int)
carts = []

for y, row in enumerate(rows):
    for x, char in enumerate(row.rstrip()):
        if char == '-':
            tracks[y][x] = 1
        elif char == '|':
            tracks[y][x] = 2
        elif char == '/':
            tracks[y][x] = 3
        elif char == '\\':
            tracks[y][x] = 4
        elif char == '+':
            tracks[y][x] = 5
        elif char == '<':
            tracks[y][x] = 1
            carts.append(Cart(x, y, -1, 0))
        elif char == '>':
            tracks[y][x] = 1
            carts.append(Cart(x, y, 1, 0))
        elif char == '^':
            tracks[y][x] = 2
            carts.append(Cart(x, y, 0, -1))
        elif char == 'v':
            tracks[y][x] = 2
            carts.append(Cart(x, y, 0, 1))
        else:
            assert char == ' ', char


def part1():
    while True:
        for cart in sorted(carts, key=lambda c: len(carts) * c.y + c.x):
            cart.x += cart.dx
            cart.y += cart.dy

            for c in carts:
                if c != cart and c.x == cart.x and c.y == cart.y:
                    return cart.x, cart.y

            track = tracks[cart.y][cart.x]
            if track == 3:
                if cart.dx != 0:
                    cart.turn_left()
                else:
                    cart.turn_right()
            elif track == 4:
                if cart.dx != 0:
                    cart.turn_right()
                else:
                    cart.turn_left()
            elif track == 5:
                cart.intersection()


def part1():
    while len(carts) > 1:
        for cart in sorted(carts, key=lambda c: len(carts) * c.y + c.x):
            cart.x += cart.dx
            cart.y += cart.dy

            for c in carts:
                if c != cart and c.x == cart.x and c.y == cart.y:
                    carts.remove(c)
                    carts.remove(cart)

            track = tracks[cart.y][cart.x]
            if track == 3:
                if cart.dx != 0:
                    cart.turn_left()
                else:
                    cart.turn_right()
            elif track == 4:
                if cart.dx != 0:
                    cart.turn_right()
                else:
                    cart.turn_left()
            elif track == 5:
                cart.intersection()

    return carts[0].x, carts[0].y


print(part1())

