import streamlit as st
import chess
import chess.svg
from generator import PuzzleGenerator

# Load puzzles once
@st.cache_data
def load_puzzles():
    gen = PuzzleGenerator("engine\stockfish-windows-x86-64-avx2.exe")
    return gen.generate_puzzle(r"games\sample.pgn")


puzzles = load_puzzles()

# Session state
if "index" not in st.session_state:
    st.session_state.index = 0
if "show_solution" not in st.session_state:
    st.session_state.show_solution = False

puzzle = puzzles[st.session_state.index]

st.title("♟️ Chess Puzzle Trainer")

st.markdown(f"### Puzzle {st.session_state.index + 1}")
st.markdown(f"Side to move: **{puzzle.side_to_move}**")

# Show board
board = chess.Board(puzzle.fen)
svg = chess.svg.board(board=board, size=400)
st.components.v1.html(svg, height=450)

# Buttons
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Show Solution"):
        st.session_state.show_solution = True

with col2:
    if st.button("Next Puzzle"):
        st.session_state.index = (st.session_state.index + 1) % len(puzzles)
        st.session_state.show_solution = False

with col3:
    if st.button("Previous"):
        st.session_state.index = max(0, st.session_state.index - 1)
        st.session_state.show_solution = False

# Show solution
if st.session_state.show_solution:
    st.success(f"Best move: {puzzle.best_move}")
    st.write(f"Evaluation: {puzzle.evaluation}")
