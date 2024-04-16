from enum import Enum
import random

pairs = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)]

diag_directions = [(2, -1, -1), (1, -2, 1), (-1, -1, 2), (-2, 1, 1), (-1, 2, -1), (1, 1, -2)]

directions = [(1, 0, -1), (1, -1, 0), (0, -1, 1), (-1, 0, 1), (-1, 1, 0), (0, 1, -1)]


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
    TWO = (2, 1)
    THREE = (3, 2)
    FOUR = (4, 3)
    FIVE = (5, 4)
    SIX = (6, 5)
    SEVEN = (7, 6)
    EIGHT = (8, 5)
    NINE = (9, 4)
    TEN = (10, 3)
    ELEVEN = (11, 2)
    TWELVE = (12, 1)


def coords_add(a, b):
    result = tuple(a[i] + b[i] for i in range(3))
    return result


def coords_sub(a, b):
    result = tuple(a[i] - b[i] for i in range(3))
    return result


def coords_scale(a, k):
    result = tuple(a[i] * k for i in range(3))
    return result


def get_neighbor_coords(coords, direction):
    return coords_add(coords, directions[direction])


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


def init_vertices(seed):
    vertex_list = list()
    for coords in Board.coords_set:
        for pair in pairs:
            vertex_coords = set()
            vertex_coords.add(coords)
            d1, d2 = pair

            if valid_coords(2, get_neighbor_coords(coords, d1)):
                vertex_coords.add(get_neighbor_coords(coords, d1))

            if valid_coords(2, get_neighbor_coords(coords, d2)):
                vertex_coords.add(get_neighbor_coords(coords, d2))

            current_vertex = Vertex(frozenset(vertex_coords))

            if current_vertex not in vertex_list or len(current_vertex.tile_coords) == 1:
                vertex_list.append(current_vertex)

    # ACCOUNT FOR PORTS VS WATER

    return vertex_list


def init_tiles(seed):
    random.seed(seed)

    materials = [Material.WOOD] * 4 + [Material.WHEAT] * 4 + [Material.ORE] * 3 + [Material.BRICK] * 3 + [
        Material.SHEEP] * 4 + [Material.DESERT] * 1

    numbers = [Number.TWO] * 2 + [Number.THREE] * 2 + [Number.FOUR] * 2 + [Number.FIVE] * 2 + [Number.SIX] * 2 + [
        Number.EIGHT] * 2 + [Number.NINE] * 2 + [Number.TEN] * 2 + [Number.ELEVEN] * 2 + [Number.TWELVE] * 2

    tile_dict = {}

    for coords in Board.coords_set:
        material = random.sample(materials, 1)[0]
        materials.remove(material)
        if material == material.DESERT:
            number = 7
        else:
            number = random.sample(numbers, 1)[0]
            numbers.remove(number)
        tile_dict[(coords[0], coords[1], coords[2])] = Tile((coords[0], coords[1], coords[2]), material, number)
    return tile_dict


class Tile:
    def __init__(self, coords, material, number):
        self.coords = coords
        self.material = material
        self.number = number

    def __str__(self):
        return f"Tile:\n  Board Coordinates: {self.coords}\n  Material: {self.material}\n  Number: {self.number}"

    def __eq__(self, other):
        if isinstance(other, Tile):
            return self.coords == other.coords and self.material == other.material and self.number == other.number
        return False


class Vertex:
    def __init__(self, tile_coords):
        self.tile_coords = tile_coords

    def __str__(self):
        tile_coords_str = ' || '.join(str(coord) for coord in self.tile_coords)
        return f"Vertex:\n  Tile Coordinates: {tile_coords_str}\n"

    def __eq__(self, other):
        if isinstance(other, Vertex):
            return self.tile_coords == other.tile_coords
        return False


class Board:
    N = 2
    coords_set = set()
    vertex_list = list()

    for q in range(-N, N + 1):
        for r in range(-N, N + 1):
            for s in range(-N, N + 1):
                if q + r + s == 0:
                    coords_set.add((q, r, s))

    def __init__(self, seed):
        self.tile_dict = init_tiles(seed)
        self.vertex_list = init_vertices(seed)
