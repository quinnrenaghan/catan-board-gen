import collections

BoardHex = collections.namedtuple("Hex", ["q", "r", "s"])

BoardVertex = collections.namedtuple("Vertex", ["hexes"])


def Hex(q, r, s):
    return BoardHex(q, r, s)


def Vertex(hex_set):
    return BoardVertex(hex_set)


def hex_add(a, b):
    return Hex(a.q + b.q, a.r + b.r, a.s + b.s)


def hex_subtract(a, b):
    return Hex(a.q - b.q, a.r - b.r, a.s - b.s)


def hex_scale(a, k):
    return Hex(a.q * k, a.r * k, a.s * k)


def hex_rotate_left(a):
    return Hex(-a.s, -a.q, -a.r)


def hex_rotate_right(a):
    return Hex(-a.r, -a.s, -a.q)


hex_directions = [Hex(1, 0, -1), Hex(1, -1, 0), Hex(0, -1, 1), Hex(-1, 0, 1), Hex(-1, 1, 0), Hex(0, 1, -1)]
pairs = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)]


def hex_direction(direction):
    return hex_directions[direction]


def hex_neighbor(hex, direction):
    return hex_add(hex, hex_direction(direction))


hex_diagonals = [Hex(2, -1, -1), Hex(1, -2, 1), Hex(-1, -1, 2), Hex(-2, 1, 1), Hex(-1, 2, -1), Hex(1, 1, -2)]


def hex_diagonal_neighbor(hex, direction):
    return hex_add(hex, hex_diagonals[direction])


def hex_length(hex):
    return (abs(hex.q) + abs(hex.r) + abs(hex.s)) // 2


def hex_distance(a, b):
    return hex_length(hex_subtract(a, b))


def valid_hex(max_range, curr_hex):
    if -max_range <= curr_hex.q <= max_range and -max_range <= curr_hex.r <= max_range and -max_range <= curr_hex.s <= max_range:
        return True
    else:
        return False


def equal_hex(a, b):
    if a.q == b.q and a.s == b.s and a.r == b.r:
        return True
    return False


def equal_vertex(a, b):
    if a.hexes == b.hexes:
        return True
    return False
