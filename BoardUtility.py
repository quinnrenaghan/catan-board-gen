from enum import Enum


class Tile:
    def __init__(self, coords, material, number):
        self.coords = coords
        self.material = material
        self.number = number

    def __str__(self):
        return f"Tile:\n  Board Coordinates: {self.coords}\n  Material: {self.material}\n  Number: {self.number}"


class Vertex:
    def __init__(self, tile_coords):
        self.tile_coords = tile_coords

    def __str__(self):
        return f"Vertex:\n  Tile Coordinates: {self.tile_coords}\n"

    def __eq__(self, other):
        if isinstance(other, Vertex):
            return self.tile_coords == other.tile_coords
        return False


class Material(Enum):
    DESERT = "DESERT"
    BRICK = "BRICK"
    ORE = "ORE"
    WOOD = "WOOD"
    SHEEP = "SHEEP"
    WHEAT = "WHEAT"

    def __str__(self):
        return self.value


class Number(Enum):
    TWO = 1
    THREE = 2
    FOUR = 3
    FIVE = 4
    SIX = 5
    SEVEN = 6
    EIGHT = 5
    NINE = 4
    TEN = 3
    ELEVEN = 2
    TWELVE = 1


def coords_add(a, b):
    result = tuple(a[i] + b[i] for i in range(3))
    return result


def coords_sub(a, b):
    result = tuple(a[i] - b[i] for i in range(3))
    return result


def coords_scale(a, k):
    result = tuple(a[i] * k for i in range(3))
    return result


directions = [(1, 0, -1), (1, -1, 0), (0, -1, 1), (-1, 0, 1), (-1, 1, 0), (0, 1, -1)]
pairs = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)]


def get_neighbor_coords(coords, direction):
    return coords_add(coords, directions[direction])


diag_directions = [(2, -1, -1), (1, -2, 1), (-1, -1, 2), (-2, 1, 1), (-1, 2, -1), (1, 1, -2)]


def get_diag_neighbor_coords(coords, direction):
    return coords_add(coords, diag_directions[direction])


def coord_length(coord):
    return (abs(coord[0]) + abs(coord[1]) + abs(coord[2])) // 2


def distance(a, b):
    return coord_length(coords_sub(a, b))


def valid_coords(max_range, coord):
    if -max_range <= coord[0] <= max_range and -max_range <= coord[1] <= max_range and -max_range <= coord[
        2] <= max_range:
        return True
    else:
        return False
