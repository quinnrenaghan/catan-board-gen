from flask import Flask, jsonify, request
from Balance import get_board
from Board import Harbor, Material

app = Flask(__name__)


def serialize_board(board, score):
    tiles = {
        str(coords): {
            "material": tile.material.name,
            "number": tile.number.value[0],
        }
        for coords, tile in board.tiles.items()
    }

    harbors = {}
    for id, v in board.vertices.items():
        for item in v.tiles:
            if isinstance(item, Harbor):
                material = item.material.value
                harbor = {"material": material, "number": item.number}
                harbors[str(id)] = harbor
    return {"tiles": tiles, "harbors": harbors, "score": score}


@app.route("/api/board")
def api_board():
    board, score = get_board()
    payload = serialize_board(board, score)
    return jsonify(payload)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
