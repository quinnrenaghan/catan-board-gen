from enum import Enum
import random

diag_directions = [(2, -1, -1), (1, -2, 1), (-1, -1, 2), (-2, 1, 1), (-1, 2, -1), (1, 1, -2)]

directions = [(1, 0, -1), (1, -1, 0), (0, -1, 1), (-1, 0, 1), (-1, 1, 0), (0, 1, -1)]


class Harbor(Enum):
    BRICK = 2
    ORE = 2
    WOOD = 2
    SHEEP = 2
    WHEAT = 2
    WILDCARD = 3

    def __str__(self):
        return self.name


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


def init_vertices():
    vertex_dict = dict()
    vertex_dict[0] = Vertex(0, [(0, 0, 0), (0, -1, 1), (1, -1, 0)], (5, 6, 1))
    vertex_dict[1] = Vertex(1, [(0, 0, 0), (1, -1, 0), (1, 0, -1)], (2, 0, 9))
    vertex_dict[2] = Vertex(2, [(0, 1, -1), (0, 0, 0), (1, 0, -1)], (3, 1, 12))
    vertex_dict[3] = Vertex(3, [(-1, 1, 0), (0, 0, 0), (0, 1, -1)], (15, 4, 2))
    vertex_dict[4] = Vertex(4, [(-1, 1, 0), (-1, 0, 1), (0, 0, 0)], (18, 5, 3))
    vertex_dict[5] = Vertex(5, [(-1, 0, 1), (0, -1, 1), (0, 0, 0)], (4, 21, 0))

    vertex_dict[6] = Vertex(6, [(0, -1, 1), (1, -2, 1), (1, -1, 0)], (0, 23, 7))
    vertex_dict[7] = Vertex(7, [(1, -1, 0), (1, -2, 1), (2, -2, 0)], (6, 25, 8))
    vertex_dict[8] = Vertex(8, [(1, -1, 0), (2, -2, 0), (2, -1, -1)], (9, 7, 28))
    vertex_dict[9] = Vertex(9, [(1, 0, -1), (1, -1, 0), (2, -1, -1)], (1, 8, 10))
    vertex_dict[10] = Vertex(10, [(1, 0, -1), (2, -1, -1), (2, 0, -2)], (11, 9, 30))
    vertex_dict[11] = Vertex(11, [(1, 1, -2), (1, 0, -1), (2, 0, -2)], (12, 10, 33))
    vertex_dict[12] = Vertex(12, [(0, 1, -1), (1, 0, -1), (1, 1, -2)], (13, 2, 11))
    vertex_dict[13] = Vertex(13, [(0, 2, -2), (0, 1, -1), (1, 1, -2)], (14, 12, 35))
    vertex_dict[14] = Vertex(14, [(-1, 2, -1), (0, 1, -1), (0, 2, -2)], (38, 15, 13))
    vertex_dict[15] = Vertex(15, [(-1, 2, -1), (-1, 1, 0), (0, 1, -1)], (16, 3, 14))
    vertex_dict[16] = Vertex(16, [(-2, 2, 0), (-1, 1, 0), (-1, 2, -1)], (40, 17, 15))
    vertex_dict[17] = Vertex(17, [(-2, 2, 0), (-2, 1, 1), (-1, 1, 0)], (43, 18, 16))
    vertex_dict[18] = Vertex(18, [(-2, 1, 1), (-1, 0, 1), (-1, 1, 0)], (17, 19, 4))
    vertex_dict[19] = Vertex(19, [(-2, 1, 1), (-2, 0, 2), (-1, 0, 1)], (45, 20, 18))
    vertex_dict[20] = Vertex(20, [(-1, -1, 2), (-2, 0, 2), (-1, 0, 1)], (19, 48, 21))
    vertex_dict[21] = Vertex(21, [(-1, -1, 2), (0, -1, 1), (-1, 0, 1)], (22, 20, 5))
    vertex_dict[22] = Vertex(22, [(0, -2, 2), (-1, -1, 2), (0, -1, 1)], (50, 23, 21))
    vertex_dict[23] = Vertex(23, [(0, -2, 2), (1, -2, 1), (0, -1, 1)], (53, 22, 6))

    vertex_dict[24] = Vertex(24, [(1, -2, 1)], (53, 25))
    vertex_dict[25] = Vertex(25, [(1, -2, 1), (2, -2, 0)], (24, 26, 7))
    vertex_dict[26] = Vertex(26, [(2, -2, 0)], (25, 27))
    vertex_dict[27] = Vertex(27, [(2, -2, 0)], (26, 28))
    vertex_dict[28] = Vertex(28, [(2, -2, 0), (2, -1, -1)], (27, 8, 29))
    vertex_dict[29] = Vertex(29, [(2, -1, -1)], (28, 30))
    vertex_dict[30] = Vertex(30, [(2, -1, -1), (2, 0, -2)], (10, 29, 31))
    vertex_dict[31] = Vertex(31, [(2, 0, -2)], (30, 32))
    vertex_dict[32] = Vertex(32, [(2, 0, -2)], (31, 33))
    vertex_dict[33] = Vertex(33, [(2, 0, -2), (1, 1, -2)], (11, 32, 34))
    vertex_dict[34] = Vertex(34, [(1, 1, -2)], (33, 35))
    vertex_dict[35] = Vertex(35, [(1, 1, -2), (0, 2, -2)], (13, 34, 36))
    vertex_dict[36] = Vertex(36, [(0, 2, -2)], (35, 37))
    vertex_dict[37] = Vertex(37, [(0, 2, -2)], (36, 38))
    vertex_dict[38] = Vertex(38, [(0, 2, -2), (-1, 2, -1)], (37, 39, 14))
    vertex_dict[39] = Vertex(39, [(-1, 2, -1)], (38, 40))
    vertex_dict[40] = Vertex(40, [(-1, 2, -1), (-2, 2, 0)], (16, 39, 41))
    vertex_dict[41] = Vertex(41, [(-2, 2, 0)], (40, 42))
    vertex_dict[42] = Vertex(42, [(-2, 2, 0)], (41, 43))
    vertex_dict[43] = Vertex(43, [(-2, 2, 0), (-2, 1, 1)], (17, 42, 44))
    vertex_dict[44] = Vertex(44, [(-2, 1, 1)], (43, 45))
    vertex_dict[45] = Vertex(45, [(-2, 1, 1,), (-2, 0, 2)], (44, 46, 19))
    vertex_dict[46] = Vertex(46, [(-2, 0, 2)], (45, 47))
    vertex_dict[47] = Vertex(47, [(-2, 0, 2)], (46, 48))
    vertex_dict[48] = Vertex(48, [(-2, 0, 2), (-1, -1, 2)], (20, 47, 49))
    vertex_dict[49] = Vertex(49, [(-1, -1, 2)], (48, 50))
    vertex_dict[50] = Vertex(50, [(-1, -1, 2), (0, -2, 2)], (49, 22, 51))
    vertex_dict[51] = Vertex(51, [(0, -2, 2)], (50, 52))
    vertex_dict[52] = Vertex(52, [(0, -2, 2)], (51, 53))
    vertex_dict[53] = Vertex(53, [(0, -2, 2), (1, -2, 1)], (52, 24, 23))

    edge_vertex_counter = 51
    edge_pieces = [[0, 0, 1, 0]] * 3 + [[1, 0, 1]] * 3
    ports = [Harbor.WILDCARD] * 4 + [Harbor.WHEAT] + [Harbor.BRICK] + [Harbor.ORE] + [Harbor.SHEEP] + [Harbor.WOOD]
    for piece_num in range(6):
        piece = random.sample(edge_pieces, 1)[0]
        edge_pieces.remove(piece)
        for vertex in piece:
            if vertex == 1:
                port = random.sample(ports, 1)[0]
                ports.remove(port)
                vertex_dict[edge_vertex_counter].tile_coords.append(port)

                if edge_vertex_counter == 53:
                    edge_vertex_counter = 23

                vertex_dict[edge_vertex_counter + 1].tile_coords.append(port)
                edge_vertex_counter += 2
            else:
                edge_vertex_counter += 1

            if edge_vertex_counter == 54:
                edge_vertex_counter = 24
    return vertex_dict


def init_tiles():
    materials = [Material.WOOD] * 4 + [Material.WHEAT] * 4 + [Material.ORE] * 3 + [Material.BRICK] * 3 + [
        Material.SHEEP] * 4 + [Material.DESERT] * 1

    numbers = [Number.TWO] * 2 + [Number.THREE] * 2 + [Number.FOUR] * 2 + [Number.FIVE] * 2 + [Number.SIX] * 2 + [
        Number.EIGHT] * 2 + [Number.NINE] * 2 + [Number.TEN] * 2 + [Number.ELEVEN] * 2 + [Number.TWELVE] * 2

    tile_dict = {}

    for coords in Board.coords_set:
        material = random.sample(materials, 1)[0]
        materials.remove(material)
        if material == material.DESERT:
            number = Number.SEVEN
        else:
            number = random.sample(numbers, 1)[0]
            numbers.remove(number)
        tile_dict[(coords[0], coords[1], coords[2])] = Tile(material, number)
    return tile_dict


class Tile:
    def __init__(self, material, number):
        self.material = material
        self.number = number

    def __str__(self):
        return f"{self.material}:{self.number.value[0]}"

    def __eq__(self, other):
        if isinstance(other, Tile):
            return self.material == other.material and self.number == other.number
        return False


class Vertex:
    def __init__(self, vertex_id, tile_coords, neighbor_vertices):
        self.vertex_id = vertex_id
        self.tile_coords = tile_coords
        self.neighbor_vertices = neighbor_vertices
        self.occupied = False
        self.strength = 0

    def __str__(self):
        tile_coords_str = ','.join(str(coord) for coord in self.tile_coords)
        neighbor_vertex_str = ','.join(str(vertex) for vertex in self.neighbor_vertices)
        return f"Vertex {self.vertex_id}:\n  Tile Coordinates: {tile_coords_str}\n  Neighboring Vertices: {neighbor_vertex_str}"

    def __eq__(self, other):
        if isinstance(other, Vertex):
            return self.tile_coords == other.tile_coords and self.vertex_id == other.vertex_id and self.neighbor_vertices == other.neighbor_vertices
        return False


class Board:
    N = 2
    coords_set = set()

    for q in range(-N, N + 1):
        for r in range(-N, N + 1):
            for s in range(-N, N + 1):
                if q + r + s == 0:
                    coords_set.add((q, r, s))

    def __init__(self):
        self.tile_dict = init_tiles()
        self.vertex_dict = init_vertices()

    def __str__(self):
        sorted_items = sorted(self.tile_dict.items(), key=lambda x: (x[0][1], x[0][0]))
        pattern = [3, 4, 5, 4, 3]
        big_string = ""
        idx = 0
        for num_items in pattern:
            small_string = ""
            for i in range(num_items):
                small_string += " " + str(sorted_items[idx][1])
                idx = idx + 1
            big_string += small_string.center(50)
            big_string += "\n"
        return big_string
