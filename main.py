from fastapi import FastAPI, HTTPException
from typing import List
import random
import numpy as np
from sudoku import generate_sudoku

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Sudoku API!"}

@app.get("/generate/{difficulty}")
def generate_sudoku_puzzle(difficulty: str):
    """
    Endpoint to generate a Sudoku puzzle based on the difficulty level.
    difficulty can be 'easy', 'intermediate', or 'hard'.
    """
    if difficulty not in ["easy", "intermediate", "hard"]:
        raise HTTPException(status_code=400, detail="Difficulty must be 'easy', 'intermediate', or 'hard'")

    # Generate a Sudoku puzzle for the given difficulty
    puzzle = generate_sudoku(difficulty)

    return {"difficulty": difficulty, "puzzle": puzzle}
