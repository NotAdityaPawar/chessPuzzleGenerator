from dataclasses import dataclass


@dataclass
class Puzzle:
    fen: str
    best_move: str
    evaluation: int
    side_to_move: str
    continuation: list
    difficulty: int
    
    
    
