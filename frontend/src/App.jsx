import { useState } from "react";
import "./App.css";
import HexBoard from "./HexBoard.jsx";
import Tippy from '@tippyjs/react'
import 'tippy.js/dist/tippy.css';


async function fetchBoard() {
  setLoading(true);
  const res = await fetch("https://catan-board-gen.onrender.com/api/board");
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
        <div style={{ marginTop: 12 }}>
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
                    <Tippy content="The lower the score, the more balanced the board. Scores less than 1 are considered extremely balanced (~ 1 in every 100 boards)." placement="top" arrow={true}>
                      <span className="info-icon" aria-hidden>
                        <svg viewBox="0 0 24 24" width="16" height="16" fill="none" xmlns="http://www.w3.org/2000/svg" focusable="false" aria-hidden="true">
                          <circle cx="12" cy="12" r="10" stroke="rgba(255,255,255,0.18)" strokeWidth="1.5" fill="transparent"/>
                          <path d="M12 8h.01M11 12h2v4h-2z" stroke="#fff" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"/>
                        </svg>
                      </span>
                    </Tippy>
                </div>
                <span className="score-value">{Number(board.score).toFixed(3)}</span>
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
