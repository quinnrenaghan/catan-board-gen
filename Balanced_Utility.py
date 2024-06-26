import Board_Utility as Util
import numpy as np


def get_board(minutes):
    boards_per_second = 10000.00 / 5
    seconds = minutes * 60
    num_boards = int(boards_per_second * seconds)

    best_board = Util.Board()
    best_score = sum(balance_score(best_board))

    for num in range(num_boards):
        board = Util.Board()
        score = sum(balance_score(board))
        if score < best_score:
            best_score = score
            best_board = board
    return best_board


def harbor_score_helper(board, vertex):
    score = 0
    harbor_vertex = board.vertex_dict[vertex]

    for coords in harbor_vertex.tile_coords:
        if isinstance(coords, Util.Harbor):
            material = coords.value[1]

    for coords in harbor_vertex.tile_coords:
        if not isinstance(coords, Util.Harbor):
            tile = board.tile_dict[coords]
            if material == "wildcard" and tile.material != Util.Material.DESERT:
                score += tile.number.value[1] * 2
            elif tile.material == material:
                score += tile.number.value[1] * 4
            elif tile.material != Util.Material.DESERT:
                score += tile.number.value[1] * 1

    for adjacent in harbor_vertex.neighbor_vertices:
        neighbor = board.vertex_dict[adjacent]
        for coords in neighbor.tile_coords:
            if not isinstance(coords, Util.Harbor):
                tile = board.tile_dict[coords]
                if material == "wildcard" and tile.material != Util.Material.DESERT:
                    score += tile.number.value[1]
                elif tile.material == material:
                    score += tile.number.value[1] * 2

    return score


def harbor_score(board):
    scores = list()
    edge_vertex = 51

    while edge_vertex != 50:
        if any(isinstance(tile, Util.Harbor) for tile in board.vertex_dict[edge_vertex].tile_coords):
            first_vertex = edge_vertex
            edge_vertex += 1
            if edge_vertex == 54:
                edge_vertex = 24

            second_vertex = edge_vertex
            edge_vertex += 1
            if edge_vertex == 54:
                edge_vertex = 24

            scores.append(max(harbor_score_helper(board, first_vertex), harbor_score_helper(board, second_vertex)))
        else:
            edge_vertex += 1
            if edge_vertex == 54:
                edge_vertex = 24

    squared_differences = list()
    average = np.mean(scores)
    for score in scores:
        squared_differences.append((score - average) * (score - average))

    return np.mean(squared_differences)


def number_clustering(board):
    total = 0
    high_prio = [Util.Number.SIX, Util.Number.EIGHT]
    for tile_coord in board.coords_set:
        tile = board.tile_dict[tile_coord]
        for direction in range(6):
            if Util.valid_coord(Util.get_neighbor_coords(tile_coord, direction)):
                neighbor = board.tile_dict[Util.get_neighbor_coords(tile_coord, direction)]
                if neighbor.number in high_prio and tile.number in high_prio:
                    total += 10
                elif neighbor.number == tile.number:
                    total += 1
    return total


def probability_distribution(board):
    total = 0
    for axis in range(3):
        total += probability_distribution_helper(board, axis)
    return total


def probability_distribution_helper(board, axis):
    positive_total = 0
    negative_total = 0
    for tile_coord in board.coords_set:
        tile = board.tile_dict[tile_coord]
        if tile.material != Util.Material.DESERT:
            if tile_coord[axis] > 0:
                positive_total += tile.number.value[1]
            elif tile_coord[axis] < 0:
                negative_total += tile.number.value[1]
            else:
                positive_total += tile.number.value[1] / 2
                negative_total += tile.number.value[1] / 2
    return (positive_total - negative_total) * (positive_total - negative_total)


def resource_probability(board):
    total = 0
    for material in Util.Material:
        if material != Util.Material.DESERT:
            total += resource_probability_helper(board, material)
    return total


def resource_probability_helper(board, material):
    total = 0
    if material == Util.Material.ORE or material == Util.Material.BRICK:
        expected = 9.667
    else:
        expected = 12.889
    for tile_coord in board.coords_set:
        tile = board.tile_dict[tile_coord]
        if tile.material == material:
            total += tile.number.value[1]
    return (total - expected) * (total - expected)


def resource_clustering(board):
    total = 0
    for tile_coord in board.coords_set:
        tile = board.tile_dict[tile_coord]
        for direction in range(6):
            if Util.valid_coord(Util.get_neighbor_coords(tile_coord, direction)):
                neighbor = board.tile_dict[Util.get_neighbor_coords(tile_coord, direction)]
                if neighbor.material == tile.material:
                    total += 1
    return total


def resource_distribution(board):
    total = 0
    for axis in range(3):
        for material in Util.Material:
            total += resource_distribution_helper(board, material, axis)
    return total


def resource_distribution_helper(board, material, axis):
    positive_total = 0
    negative_total = 0
    for tile_coord in board.coords_set:
        tile = board.tile_dict[tile_coord]
        if tile.material == material and tile.material != Util.Material.DESERT:
            if tile_coord[axis] > 0:
                positive_total += 6
            elif tile_coord[axis] < 0:
                negative_total += 6
            else:
                positive_total += 3
                negative_total += 3
    return (positive_total - negative_total) * (positive_total - negative_total)


def balance_score(board):
    normalized_scores = list()

    harbor_val = harbor_score(board)
    number_clustering_val = number_clustering(board)
    probability_distribution_val = probability_distribution(board)
    resource_probability_val = resource_probability(board)
    resource_clustering_val = resource_clustering(board)
    resource_distribution_val = resource_distribution(board)

    normalized_scores.append(harbor_val / 1000.00)
    normalized_scores.append(number_clustering_val / 115.00)
    normalized_scores.append(probability_distribution_val / 875.00)
    normalized_scores.append(resource_probability_val / 155.00)
    normalized_scores.append(resource_clustering_val / 40.00)
    normalized_scores.append(resource_distribution_val / 4350.00)

    return normalized_scores
