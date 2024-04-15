import BoardUtility as bu

tile_dict = dict()
vertex_list = list()


def setup_board():
    n = 2
    for q in range(-n, n + 1):
        for r in range(-n, n + 1):
            for s in range(-n, n + 1):
                if q + r + s == 0:
                    tile_dict[(q, r, s)] = bu.Tile((q, r, s), bu.Material.BRICK, bu.Number.SIX)

    for curr_tile in tile_dict.values():
        curr_coords = curr_tile.coords
        for pair in bu.pairs:
            vertex_coords = set()
            vertex_coords.add(curr_coords)
            d1, d2 = pair

            if bu.valid_coords(2, bu.get_neighbor_coords(curr_coords, d1)):
                vertex_coords.add(bu.get_neighbor_coords(curr_coords, d1))

            if bu.valid_coords(2, bu.get_neighbor_coords(curr_coords, d2)):
                vertex_coords.add(bu.get_neighbor_coords(curr_coords, d2))

            current_vertex = bu.Vertex(frozenset(vertex_coords))

            if current_vertex not in vertex_list or len(current_vertex.tile_coords) == 1:
                vertex_list.append(current_vertex)