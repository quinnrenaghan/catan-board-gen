from Board import Board, Harbor, Material, Number, BOARD_COORDS

def harbor_score(board):
    total = 0.0
    vertices = board.vertices.values()
    for vertex in vertices:
        tiles = vertex.tiles
        harbor = next((h for h in tiles if isinstance(h, Harbor)), None)
        if harbor is None or harbor.material is Material.WILDCARD:
            continue
        for t in tiles:
            if isinstance(t, Harbor):
                continue
            if t.material is harbor.material:
                total += t.number.probability
    return total


def resource_probability(board):
    total = 0.0
    for material in Material:
        if material is not Material.DESERT:
            total += resource_probability_helper(board, material)
    return total

def resource_probability_helper(board, material):
    EXPECTED_COMMON = 12.889
    EXPECTED_RARE = 9.667
    total = 0.0
    if material == Material.ORE or material == Material.BRICK:
        expected = EXPECTED_RARE
    else:
        expected = EXPECTED_COMMON
    for coords in BOARD_COORDS:
        tile = board.tiles[coords]
        if tile.material == material:
            total += tile.number.probability
    return (total - expected) * (total - expected)


def resource_clustering(board):
    total = 0.0
    vertices = board.vertices.values()
    for vertex in vertices:
        tiles = vertex.tiles
        for i in range(len(tiles)):
            for j in range(i + 1, len(tiles)):
                tile_a = tiles[i]
                tile_b = tiles[j]
                if tile_a.material == tile_b.material:
                    total += 1
    return total

def number_clustering(board):
    PRIO_NUMBERS = (Number.SIX, Number.EIGHT)
    total = 0.0
    vertices = board.vertices.values()
    for vertex in vertices:
        tiles = vertex.tiles
        for i in range(len(tiles)):
            for j in range(i + 1, len(tiles)):
                tile_a = tiles[i]
                tile_b = tiles[j]
                if tile_a.number == tile_b.number or (tile_a.number in PRIO_NUMBERS and tile_b.number in PRIO_NUMBERS):
                    total += 1
    return total

def resource_distribution(board):
    total = 0.0
    for axis in range(3):
        for material in Material:
            if material is not Material.DESERT:
                total += resource_distribution_helper(board, material, axis)
    return total


def resource_distribution_helper(board, material, axis):
    pos_total, neg_total = 0.0, 0.0
    for coords in BOARD_COORDS:
        tile = board.tiles[coords]
        if tile.material is material:
            if coords[axis] > 0:
                pos_total += 1.0
            elif coords[axis] < 0:
                neg_total += 1.0
            else:
                pos_total += 0.5
                neg_total += 0.5
    return (pos_total - neg_total) * (pos_total - neg_total)

def probability_distribution(board):
    total = 0.0
    for axis in range(3):
        total += probability_distribution_helper(board, axis)
    return total


def probability_distribution_helper(board, axis):
    pos_total = 0.0
    neg_total = 0.0
    for coords in BOARD_COORDS:
        tile = board.tiles[coords]
        if tile.material != Material.DESERT:
            if coords[axis] > 0:
                pos_total += tile.number.probability
            elif coords[axis] < 0:
                neg_total += tile.number.probability
            else:
                pos_total += tile.number.probability / 2
                neg_total += tile.number.probability / 2
    return (pos_total - neg_total) * (pos_total - neg_total)

def balance(board):
    MAX_HARBOR = 60.0
    MAX_NUMBER_CLUSTERING = 25.0
    MAX_PROBABILITY_DISTRIBUTION = 900.0
    MAX_RESOURCE_PROBABILITY = 350.0
    MAX_RESOURCE_CLUSTERING = 50.0
    MAX_RESOURCE_DISTRIBUTION = 125.0
    score = 0.0
    score += (harbor_score(board)) / MAX_HARBOR + number_clustering(board) / MAX_NUMBER_CLUSTERING + probability_distribution(board) / MAX_PROBABILITY_DISTRIBUTION + resource_probability(board) / MAX_RESOURCE_PROBABILITY + resource_clustering(board) / MAX_RESOURCE_CLUSTERING + resource_distribution(board) / MAX_RESOURCE_DISTRIBUTION
    return score

def get_board():
    board = Board()
    balance_score = balance(board)
    return board, balance_score 
