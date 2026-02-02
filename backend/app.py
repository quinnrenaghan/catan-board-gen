from flask import Flask, jsonify
from flask_cors import CORS
from Balance import get_board
from Board import Harbor
import os

app = Flask(__name__)
CORS(app, origins=["https://quinnrenaghan.github.io"])    

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
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
