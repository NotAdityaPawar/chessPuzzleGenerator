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
        prev_eval = 0
        
        # print(game.mainline_moves())
        
        for move in game.mainline_moves():
            board.push(move)
            
            fen = board.fen()
            
            
            current_eval = self.eval.evaluate(fen)
            
            if current_eval['type'] != 'cp':
                continue
            
            
            value = current_eval['value']
            
            if abs(value - prev_eval) > THRESHOLD:
                best = self.eval.best_move(fen)
                
                # print(f"value {value}")
                puzzle = Puzzle(
                    fen = fen, 
                    best_move= best,
                    evaluation= value, 
                    side_to_move="white" if board.turn else "black",
                    continuation=[best],
                    difficulty= min(2400, max(400, 800 + abs(value)))
                )
                puzzles.append(puzzle)
                
        
            prev_eval = value
            
        return puzzles
    
    