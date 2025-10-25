import React from "react";
import "./HexBoard.css";

const MATERIAL_COLORS = {
  WOOD: "#2e8b57",
  WHEAT: "#f8c91dff",
  ORE: "#393a3bff",
  BRICK: "#cf531eff",
  SHEEP: "#bfe6a0",
  DESERT: "#e7d7b7",
};

function parseCoord(key) {
  const cleaned = key.replace(/[()]/g, "");
  return cleaned.split(",").map((s) => Number(s.trim()));
}

function cubeToPixel(cube, size) {
  const q = cube[0];
  const r = cube[1];
  const x = size * Math.sqrt(3) * (q + r / 2);
  const y = size * (3 / 2) * r;
  return [x, y];
}

function hexPolygon(x, y, size) {
  const points = [];
  for (let i = 0; i < 6; i++) {
    const angle_deg = 60 * i - 30;
    const angle_rad = (Math.PI / 180) * angle_deg;
    const px = x + size * Math.cos(angle_rad);
    const py = y + size * Math.sin(angle_rad);
    points.push(`${px},${py}`);
  }
  return points.join(" ");
}

export default function HexBoard({
  board,
  size = 50,           
  numberRadius = 18,   
  numberFontSize = 20, 
}) {
  if (!board || !board.tiles) return null;

  const tiles = Object.entries(board.tiles).map(([k, t]) => {
    const cube = parseCoord(k);
    const [x, y] = cubeToPixel(cube, size);
    return { key: k, cube, x, y, tile: t };
  });

  const xs = tiles.map((t) => t.x);
  const ys = tiles.map((t) => t.y);
  const padding = size * 2;
  const minX = Math.min(...xs) - padding;
  const maxX = Math.max(...xs) + padding;
  const minY = Math.min(...ys) - padding;
  const maxY = Math.max(...ys) + padding;
  const width = maxX - minX || 1;
  const height = maxY - minY || 1;

  return (
      <svg
        viewBox={`${minX} ${minY} ${width} ${height}`}
        preserveAspectRatio="xMidYMid meet"
      >
        {tiles.map(({ key, x, y, tile }) => {
          const color = MATERIAL_COLORS[tile.material] || MATERIAL_COLORS.DESERT;
          const number = Number(tile.number);
          const circleR = numberRadius;
          const fontSize = numberFontSize;
          return (
            <g key={key}>
              <polygon
                className="hex-tile"
                points={hexPolygon(x, y, size)}
                fill={color}
                stroke="#ffffff33"
                strokeWidth={2}
              />
              {tile.material !== "DESERT" && (
                <>
                  <circle
                    className="number-circle"
                    cx={x}
                    cy={y}
                    r={circleR}
                  />
                  <text
                    className="number-text"
                    x={x}
                    y={y}
                    textAnchor="middle"
                    dominantBaseline="middle"
                    style={{ fontSize: `${fontSize}px` }}
                  >
                    {number}
                  </text>
                </>
              )}
            </g>
          );
        })}
      </svg>
  );
}
