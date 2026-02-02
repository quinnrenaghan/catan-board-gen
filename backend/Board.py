from enum import Enum
import random

NEIGHBOR_DIRECTIONS = [(1, 0, -1), (1, -1, 0), (0, -1, 1), (-1, 0, 1), (-1, 1, 0), (0, 1, -1)]
EXTENDED_NEIGHBOR_DIRECTIONS = [(2, -1, -1), (1, -2, 1), (-1, -1, 2), (-2, 1, 1), (-1, 2, -1), (1, 1, -2)]
BOARD_COORDS = {
    (-2, 0, 2), (-2, 1, 1), (-2, 2, 0),
    (-1, -1, 2), (-1, 0, 1), (-1, 1, 0), (-1, 2, -1),
    (0, -2, 2), (0, -1, 1), (0, 0, 0), (0, 1, -1), (0, 2, -2),
    (1, -2, 1), (1, -1, 0), (1, 0, -1), (1, 1, -2),
    (2, -2, 0), (2, -1, -1), (2, 0, -2),
}

class Material(Enum):
    DESERT = "DESERT"
    BRICK = "BRICK"
    ORE = "ORE"
    WOOD = "WOOD"
    SHEEP = "SHEEP"
    WHEAT = "WHEAT"
    WILDCARD = "WILDCARD"

    def __str__(self):
        return self.value

class Harbor(Enum):
    BRICK = (2, Material.BRICK)
    ORE = (2, Material.ORE)
    WOOD = (2, Material.WOOD)
    SHEEP = (2, Material.SHEEP)
    WHEAT = (2, Material.WHEAT)
    WILDCARD = (3, Material.WILDCARD)

    def __init__(self, number, material):
        self.number = number
        self.material = material
    
    def __str__(self):
        return self.name


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

    def __init__(self, num, probability):
        self.num = num
        self.probability = probability

    def __str__(self):
        return self.name

def add_coords(a, b):
    result = tuple(a[i] + b[i] for i in range(3))
    return result

def sub_coords(a, b):
    result = tuple(a[i] - b[i] for i in range(3))
    return result

def scale_coords(a, k):
    result = tuple(a[i] * k for i in range(3))
    return result

def get_neighbor_coords(coords, direction):
    return add_coords(coords, NEIGHBOR_DIRECTIONS[direction])

def get_extended_neighbor_coords(coords, direction):
    return add_coords(coords, EXTENDED_NEIGHBOR_DIRECTIONS[direction])

def distance(a, b):
    diff = sub_coords(a, b)
    return (abs(diff[0]) + abs(diff[1]) + abs(diff[2])) // 2

def valid_coord(coord):
    return -2 <= coord[0] <= 2 and -2 <= coord[1] <= 2 and -2 <= coord[2] <= 2

def init_vertices(tiles):
    vertices = dict()
    vertices[0] = Vertex(0, [(0, 0, 0), (0, -1, 1), (1, -1, 0)], (5, 6, 1))
    vertices[1] = Vertex(1, [(0, 0, 0), (1, -1, 0), (1, 0, -1)], (2, 0, 9))
    vertices[2] = Vertex(2, [(0, 1, -1), (0, 0, 0), (1, 0, -1)], (3, 1, 12))
    vertices[3] = Vertex(3, [(-1, 1, 0), (0, 0, 0), (0, 1, -1)], (15, 4, 2))
    vertices[4] = Vertex(4, [(-1, 1, 0), (-1, 0, 1), (0, 0, 0)], (18, 5, 3))
    vertices[5] = Vertex(5, [(-1, 0, 1), (0, -1, 1), (0, 0, 0)], (4, 21, 0))

    vertices[6] = Vertex(6, [(0, -1, 1), (1, -2, 1), (1, -1, 0)], (0, 23, 7))
    vertices[7] = Vertex(7, [(1, -1, 0), (1, -2, 1), (2, -2, 0)], (6, 25, 8))
    vertices[8] = Vertex(8, [(1, -1, 0), (2, -2, 0), (2, -1, -1)], (9, 7, 28))
    vertices[9] = Vertex(9, [(1, 0, -1), (1, -1, 0), (2, -1, -1)], (1, 8, 10))
    vertices[10] = Vertex(10, [(1, 0, -1), (2, -1, -1), (2, 0, -2)], (11, 9, 30))
    vertices[11] = Vertex(11, [(1, 1, -2), (1, 0, -1), (2, 0, -2)], (12, 10, 33))
    vertices[12] = Vertex(12, [(0, 1, -1), (1, 0, -1), (1, 1, -2)], (13, 2, 11))
    vertices[13] = Vertex(13, [(0, 2, -2), (0, 1, -1), (1, 1, -2)], (14, 12, 35))
    vertices[14] = Vertex(14, [(-1, 2, -1), (0, 1, -1), (0, 2, -2)], (38, 15, 13))
    vertices[15] = Vertex(15, [(-1, 2, -1), (-1, 1, 0), (0, 1, -1)], (16, 3, 14))
    vertices[16] = Vertex(16, [(-2, 2, 0), (-1, 1, 0), (-1, 2, -1)], (40, 17, 15))
    vertices[17] = Vertex(17, [(-2, 2, 0), (-2, 1, 1), (-1, 1, 0)], (43, 18, 16))
    vertices[18] = Vertex(18, [(-2, 1, 1), (-1, 0, 1), (-1, 1, 0)], (17, 19, 4))
    vertices[19] = Vertex(19, [(-2, 1, 1), (-2, 0, 2), (-1, 0, 1)], (45, 20, 18))
    vertices[20] = Vertex(20, [(-1, -1, 2), (-2, 0, 2), (-1, 0, 1)], (19, 48, 21))
    vertices[21] = Vertex(21, [(-1, -1, 2), (0, -1, 1), (-1, 0, 1)], (22, 20, 5))
    vertices[22] = Vertex(22, [(0, -2, 2), (-1, -1, 2), (0, -1, 1)], (50, 23, 21))
    vertices[23] = Vertex(23, [(0, -2, 2), (1, -2, 1), (0, -1, 1)], (53, 22, 6))

    vertices[24] = Vertex(24, [(1, -2, 1)], (53, 25))
    vertices[25] = Vertex(25, [(1, -2, 1), (2, -2, 0)], (24, 26, 7))
    vertices[26] = Vertex(26, [(2, -2, 0)], (25, 27))
    vertices[27] = Vertex(27, [(2, -2, 0)], (26, 28))
    vertices[28] = Vertex(28, [(2, -2, 0), (2, -1, -1)], (27, 8, 29))
    vertices[29] = Vertex(29, [(2, -1, -1)], (28, 30))
    vertices[30] = Vertex(30, [(2, -1, -1), (2, 0, -2)], (10, 29, 31))
    vertices[31] = Vertex(31, [(2, 0, -2)], (30, 32))
    vertices[32] = Vertex(32, [(2, 0, -2)], (31, 33))
    vertices[33] = Vertex(33, [(2, 0, -2), (1, 1, -2)], (11, 32, 34))
    vertices[34] = Vertex(34, [(1, 1, -2)], (33, 35))
    vertices[35] = Vertex(35, [(1, 1, -2), (0, 2, -2)], (13, 34, 36))
    vertices[36] = Vertex(36, [(0, 2, -2)], (35, 37))
    vertices[37] = Vertex(37, [(0, 2, -2)], (36, 38))
    vertices[38] = Vertex(38, [(0, 2, -2), (-1, 2, -1)], (37, 39, 14))
    vertices[39] = Vertex(39, [(-1, 2, -1)], (38, 40))
    vertices[40] = Vertex(40, [(-1, 2, -1), (-2, 2, 0)], (16, 39, 41))
    vertices[41] = Vertex(41, [(-2, 2, 0)], (40, 42))
    vertices[42] = Vertex(42, [(-2, 2, 0)], (41, 43))
    vertices[43] = Vertex(43, [(-2, 2, 0), (-2, 1, 1)], (17, 42, 44))
    vertices[44] = Vertex(44, [(-2, 1, 1)], (43, 45))
    vertices[45] = Vertex(45, [(-2, 1, 1,), (-2, 0, 2)], (44, 46, 19))
    vertices[46] = Vertex(46, [(-2, 0, 2)], (45, 47))
    vertices[47] = Vertex(47, [(-2, 0, 2)], (46, 48))
    vertices[48] = Vertex(48, [(-2, 0, 2), (-1, -1, 2)], (20, 47, 49))
    vertices[49] = Vertex(49, [(-1, -1, 2)], (48, 50))
    vertices[50] = Vertex(50, [(-1, -1, 2), (0, -2, 2)], (49, 22, 51))
    vertices[51] = Vertex(51, [(0, -2, 2)], (50, 52))
    vertices[52] = Vertex(52, [(0, -2, 2)], (51, 53))
    vertices[53] = Vertex(53, [(0, -2, 2), (1, -2, 1)], (52, 24, 23))

    for v in vertices.values():
            v.tiles = [tiles[c] for c in v.tile_coords]

    return vertices

def init_harbors(vertices):
    vertex_id = 51

    edge_piece_single = (0, 0, 1, 0)
    edge_piece_double = (1, 0, 1)

    harbors = [Harbor.WILDCARD] * 4 + [Harbor.WHEAT] + [Harbor.BRICK] + [Harbor.ORE] + [Harbor.SHEEP] + [Harbor.WOOD]
    for piece_num in range(6):
        piece = edge_piece_double if (piece_num % 2) == 0 else edge_piece_single
        for position in piece:
            if position == 1:
                harbor = random.choice(harbors)
                harbors.remove(harbor)

                vertices[vertex_id].tiles.append(harbor)
                vertex_id += 1

                if vertex_id == 54:
                    vertex_id = 24

                vertices[vertex_id].tiles.append(harbor)
                vertex_id += 1
            else:
                vertex_id += 1
                if vertex_id == 54:
                    vertex_id = 24
    return vertices

def init_tiles():
    materials = [Material.WOOD] * 4 + [Material.WHEAT] * 4 + [Material.ORE] * 3 + [Material.BRICK] * 3 + [
        Material.SHEEP] * 4 + [Material.DESERT] * 1
    numbers = [Number.TWO] * 2 + [Number.THREE] * 2 + [Number.FOUR] * 2 + [Number.FIVE] * 2 + [Number.SIX] * 2 + [
        Number.EIGHT] * 2 + [Number.NINE] * 2 + [Number.TEN] * 2 + [Number.ELEVEN] * 2 + [Number.TWELVE] * 2

    tiles = dict()

    for coords in BOARD_COORDS:
        material = random.choice(materials)
        materials.remove(material)
        if material == Material.DESERT:
            number = Number.SEVEN
        else:
            number = random.choice(numbers)
            numbers.remove(number)
        tiles[coords] = Tile(material, number)
    return tiles  

class Vertex:
    """Board vertex: holds adjacent tile coordinates (mutable), neighbor vertex ids, occupancy and strength."""
    def __init__(self, vertex_id, tile_coords, neighbor_vertex_ids):
        self.vertex_id = vertex_id
        self.tile_coords = list(tile_coords)
        self.neighbor_vertex_ids = tuple(neighbor_vertex_ids)
        
        # runtime state
        self.tiles = []
        self.occupant = None
        self.strength = 0

class Tile:
    """Board tile: holds material and number."""
    def __init__(self, material, number):
        self.material = material
        self.number = number

    def __str__(self):
        return f"{self.material}:{self.number.num}"

class Board:
    """Catan board: encapsulates an entire board - holds tile and vertex maps."""
    def __init__(self):
        self.tiles = init_tiles()
        self.vertices = init_harbors(init_vertices(self.tiles))

    def __str__(self):
        sorted_tiles = sorted(self.tiles.items(), key=lambda x: (x[0][1], x[0][0]))
        pattern = (3, 4, 5, 4, 3)
        res = ""
        res += " " * 20 + "Board"
        res += "\n\n"
        tile = 0
        for row in pattern:
            row_string = ""
            for _ in range(row):
                row_string += " " + str(sorted_tiles[tile][1])
                tile += 1
            res += row_string.center(50)
            res += "\n"
        
        res += "\n"
        res += " " * 20 + "Harbors"
        res += "\n\n"
        harbor_vertices = [v for v in self.vertices.values() if any(isinstance(t, Harbor) for t in v.tiles)]
        for v in harbor_vertices:
            res += f"Vertex {v.vertex_id}: "
            for t in v.tiles:
                if isinstance(t, Harbor):
                    res += f"{t} "
            res += "\n"
        return res
