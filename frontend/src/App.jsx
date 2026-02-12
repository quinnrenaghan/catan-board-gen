import { useState } from "react";
import "./App.css";
import HexBoard from "./HexBoard.jsx";

const API_BASE = import.meta.env.DEV ? "" : "https://catan-board-gen.onrender.com";

const BALANCE_MIN = 0.75;
const BALANCE_MAX = 2;
const DISPLAY_MIN = 0.25;
const DISPLAY_MAX = 10;

function toDisplayScore(rawBalance) {
  const clamped = Math.max(BALANCE_MIN, Math.min(BALANCE_MAX, rawBalance));
  return DISPLAY_MIN + ((BALANCE_MAX - clamped) / (BALANCE_MAX - BALANCE_MIN)) * (DISPLAY_MAX - DISPLAY_MIN);
}

export default function App() {
  const [board, setBoard] = useState(null);
  const [loading, setLoading] = useState(false);
  const [balanceStrength, setBalanceStrength] = useState(0.64);

  const balanceThreshold = 2 - balanceStrength * (2 - 0.75);

  async function fetchBoard() {
    setLoading(true);
    const params = new URLSearchParams({ threshold: balanceThreshold });
    const res = await fetch(`${API_BASE}/api/board?${params}`);
    const json = await res.json();
    setBoard(json);
    setLoading(false);
  }

  return (
    <div className="app">
      <header className="app-header">
        <h1>Catan Board Generator</h1>
      </header>
      <div className="center-card-wrapper">
        <div className="center-card">
        <div className="controls">
          <div className="slider-group">
            <label htmlFor="balance-slider" className="slider-label">
              Balance Preference
            </label>
            <input
              id="balance-slider"
              type="range"
              min={0}
              max={1}
              step={0.05}
              value={balanceStrength}
              onChange={(e) => setBalanceStrength(Number(e.target.value))}
              className="balance-slider"
            />
            <div className="slider-hints">
              <span>Less balanced</span>
              <span>Most balanced</span>
            </div>
          </div>
          <button className="gen-button" onClick={fetchBoard} disabled={loading}>
            {loading ? "Fetching..." : (
              <>
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden>
                  <path d="M12 2v20M2 12h20" stroke="#fff" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                </svg>
                Generate Board
              </>
            )}
          </button>
        </div>

        {board ? (
          <>
            <div className="score-container">
              <div className="score-badge">
                <div className="score-label">
                  Balance Score
                </div>
                <span className="score-value">{toDisplayScore(board.score).toFixed(1)}</span>
              </div>
            </div>
            <div className="ocean-background">
              <HexBoard board={board} />
            </div>
          </>
        ) : null}
        </div>
      </div>
    </div>
  );
}
