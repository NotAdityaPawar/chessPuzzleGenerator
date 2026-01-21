import chess
import chess.pgn
from evaluator import Evaluator
from model import Puzzle


THRESHOLD = 250

class PuzzleGenerator:
    def __init__(self, stockfish_path):
        self.eval = Evaluator(stockfish_path)
        

    def generate_puzzle(self, pgn_file):
        puzzles = []
        
        with open (pgn_file) as f:
            while True:
                game = chess.pgn.read_game(f)
                if game is None:
                    break 
                puzzles.extend(self._analyze_games(game))
        return puzzles
    
    
    
    
    def _analyze_games(self, game):
        board = game.board()
        puzzles = []

        for move in game.mainline_moves():
            # Eval BEFORE move
            fen_before = board.fen()
            eval_before = self.eval.evaluate(fen_before)

            board.push(move)

            # Eval AFTER move
            fen_after = board.fen()
            eval_after = self.eval.evaluate(fen_after)

            # Only handle centipawn evals for now
            if eval_before["type"] != "cp" or eval_after["type"] != "cp":
                continue

            v1 = eval_before["value"]
            v2 = eval_after["value"]

            swing = abs(v2 - v1)

            if swing > THRESHOLD:
                best = self.eval.best_move(fen_after)

                puzzle = Puzzle(
                    fen=fen_after,
                    best_move=best,
                    evaluation=v2,
                    side_to_move="white" if board.turn else "black",
                    continuation=[best],
                    difficulty=min(2400, max(400, 800 + swing))
                )

                puzzles.append(puzzle)

                print(f"Puzzle found | swing={swing} | move={move} | best={best}")

        return puzzles
        
        