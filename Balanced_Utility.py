import Board_Utility as util


def resource_distribution(board):
    total = 0
    for axis in range(3):
        for material in util.Material:
            total += resource_distribution_helper(board, material, axis)
    return total


def resource_distribution_helper(board, material, axis):
    positive_count = 0
    negative_count = 0
    for tile_coord in board.coords_set:
        tile = board.tile_dict[tile_coord]
        if tile.material == material and tile.material != util.Material.DESERT:
            if tile_coord[axis] > 0:
                positive_count += 6
            elif tile_coord[axis] < 0:
                negative_count += 6
            else:
                positive_count += 3
                negative_count += 3
    return (positive_count - negative_count) * (positive_count - negative_count)
