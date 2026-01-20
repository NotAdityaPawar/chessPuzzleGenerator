from generator import PuzzleGenerator
from export import export_json


generator = PuzzleGenerator("engine\stockfish-windows-x86-64-avx2.exe")
puzzles = generator.generate_puzzle("games\sample.pgn")

export_json(puzzles)