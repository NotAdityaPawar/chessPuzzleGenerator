# ♟️ Chess Puzzle Trainer

A Python application that automatically generates chess puzzles from PGN game files and provides an interactive web interface for solving them.

## Features

- **Automatic Puzzle Generation**: Analyzes chess games to find positions with significant evaluation swings
- **Interactive Web Interface**: Streamlit-based UI for solving puzzles with visual chess board
- **Stockfish Integration**: Uses Stockfish engine for position evaluation and best move calculation
- **Puzzle Export**: Save generated puzzles to JSON format
- **Difficulty Rating**: Automatically assigns difficulty ratings based on evaluation swings

## Installation

### Prerequisites
- Python 3.12 or higher
- Stockfish chess engine

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd chessreview
```

2. Install dependencies using uv (recommended):
```bash
uv sync
```

Or using pip:
```bash
pip install chess stockfish streamlit
```

3. Download Stockfish engine and place it in the `engine/` directory as `stockfish-windows-x86-64-avx2.exe`

## Usage

### Generate Puzzles

Run the puzzle generator on a PGN file:

```bash
python main.py
```

This will:
- Analyze games from `games/sample.pgn`
- Generate puzzles where evaluation swings exceed 250 centipawns
- Export puzzles to `puzzles.json`

### Launch Web Interface

Start the interactive puzzle trainer:

```bash
streamlit run ui.py
```

The web interface provides:
- Visual chess board display
- Navigation between puzzles
- Solution reveal functionality
- Side-to-move indication

## Project Structure

```
chessreview/
├── engine/                 # Stockfish engine executable
├── games/                  # PGN game files
│   ├── sample.pgn
│   └── master_games.pgn
├── evaluator.py           # Chess position evaluation
├── generator.py           # Puzzle generation logic
├── model.py              # Puzzle data structure
├── export.py             # JSON export functionality
├── ui.py                 # Streamlit web interface
├── main.py               # Main puzzle generation script
└── puzzles.json          # Generated puzzles output
```

## How It Works

1. **Game Analysis**: The generator reads PGN files and analyzes each position
2. **Evaluation Swing Detection**: Identifies moves that cause significant evaluation changes (>250cp)
3. **Puzzle Creation**: Creates puzzle objects with FEN, best move, and difficulty rating
4. **Interactive Solving**: Web interface displays positions for tactical training

## Configuration

- **Threshold**: Modify `THRESHOLD` in `generator.py` to adjust puzzle sensitivity
- **Engine Path**: Update Stockfish path in generator initialization
- **Game Files**: Add PGN files to the `games/` directory

## Dependencies

- `chess`: Python chess library for game parsing and board representation
- `stockfish`: Stockfish engine interface
- `streamlit`: Web interface framework

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source. Please check the license file for details.