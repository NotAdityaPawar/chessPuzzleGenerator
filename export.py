import json

def export_json(puzzles, filename = "puzzles.json"):
    data = [p.__dict__ for p in puzzles]
    
    with open (filename, 'w') as f:
        json.dump(data, f, indent=2)
        
        
    print(f"exported puzzles to file: {filename}, total puzzles {len(puzzles)}")