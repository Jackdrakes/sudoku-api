# Sudoku API Documentation

Welcome to the **Sudoku API**! This API provides an interface to generate Sudoku puzzles of various difficulty levels. You can use the API to get a new Sudoku puzzle and choose the difficulty: `easy`, `intermediate`, or `hard`.

## Base URL

The API can be accessed at:

[`Base UrL`](https://sudoku-api-zj2t.onrender.com/) :
[`https://sudoku-api-zj2t.onrender.com/`](https://sudoku-api-zj2t.onrender.com/)

---

## Endpoints

### 1. **GET /**
**Description**:
This endpoint returns a welcome message confirming that the API is up and running.

Example Request:
```http
GET / HTTP/1.1
Host: 127.0.0.1:8000
```

Example Response:
```
{
  "message": "Welcome to the Sudoku API!"
}
```

### 2. **GET /generate/{difficulty}**
**Description**:
This endpoint generates a Sudoku puzzle based on the specified difficulty level. The difficulty parameter can be one of easy, intermediate, or hard. The generated puzzle will be returned as a list of lists, where each list represents a row of the Sudoku puzzle.

Path Parameters:
difficulty (string): The difficulty level for the puzzle. The possible values are:
- easy: Generates a puzzle with 36 clues.
- intermediate: Generates a puzzle with 30 clues.
- hard: Generates a puzzle with 24 clues.

Example Request:
```
  GET /generate/easy HTTP/1.1
  Host: 127.0.0.1:8000
```

Example Response:
```
{
  "difficulty": "easy",
  "puzzle": [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
  ]
}
```

Error Response:
```
{
  "detail": "Difficulty must be 'easy', 'intermediate', or 'hard'"
}
```

#### Status Codes:
- **200 OK:** Puzzle generated successfully.
- **400 Bad Request:** Invalid difficulty level provided.

