from stockfish import Stockfish

class Evaluator:
    def __init__(self, stockfish_path):
        self.sf = Stockfish(
                path=stockfish_path,
                parameters= {
                    "Threads": 2,
                    "Minimum Thinking Time": 30
                }
            )
        
    
    def evaluate(self, fen):
        self.sf.set_fen_position(fen)
        return self.sf.get_evaluation()
    
    
    def best_move(self, fen):
        self.sf.set_fen_position(fen)
        return self.sf.get_best_move()
    
    
    def get_top_moves(self, fen, n= 3):
        self.sf.set_fen_position(fen)
        return self.get_top_moves(fen, n)
    
    
