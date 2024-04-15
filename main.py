import Util

N = 2
hex_set = set()
for q in range(-N, N + 1):
    for r in range(-N, N + 1):
        for s in range(-N, N + 1):
            if q + r + s == 0:
                hex_set.add(Util.Hex(q, r, s))

vertex_set = set()
for curr_hex in hex_set:
    for pair in Util.pairs:
        vertex_hexes = set()
        vertex_hexes.add(curr_hex)
        d1, d2 = pair

        if Util.valid_hex(2, Util.hex_neighbor(curr_hex, d1)):
            vertex_hexes.add(Util.hex_neighbor(curr_hex, d1))

        if Util.valid_hex(2, Util.hex_neighbor(curr_hex, d2)):
            vertex_hexes.add(Util.hex_neighbor(curr_hex, d2))

        current_vertex = Util.Vertex(frozenset(vertex_hexes))

        if len(vertex_hexes) == 1 and current_vertex in vertex_set:
            vertex_hexes.add("double water")
            current_vertex = Util.Vertex(frozenset(vertex_hexes))

        if current_vertex not in vertex_set:
            vertex_set.add(current_vertex)
