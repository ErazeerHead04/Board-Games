# Obstruction Game

A Python implementation of the classic paper-and-pencil game Obstruction. This text-based, multiplayer strategy game is played on a 2D grid and allows up to 5 players.

---

## Objective

Players take turns placing their checkers on empty cells. After each move, all adjacent (8-directional) cells are automatically blocked. The player who makes the last valid move wins the game.

---

## Features

- Turn-based logic for 2–5 players
- 2D grid board (default size: 6x6)
- Randomized first player
- Automatic blocking of neighboring cells
- Input validation with column-letter + row-number format (e.g., `C3`)
- Simple terminal interface using text display

---

## Game Setup

- **Board Size**: Default is 6x6  
- **Number of Players**: Default is 2  
- **Checkers**: `['X', 'O', 'M', 'N', 'P']` (for up to 5 players)

Customize these settings by modifying the following constants at the top of the script:

```python
NUM_ROW = 6
NUM_COL = 6
NUM_PLAYERS = 2
```

Valid board size: 4x4 to 9x9  
Valid player count: 2 to 5

---

## How to Run

1. Open your terminal.
2. Navigate to the directory containing `Obstruction.py`.
3. Run the game with:

```bash
python3 Obstruction.py
```

---

## Gameplay Instructions

- Each player takes turns entering a move using a format like `B2` (column letter + row number).
- The program checks for:
  - Valid input format
  - Whether the chosen cell is unoccupied
- Once a player moves, the cell is marked with their checker, and adjacent cells are marked as blocked (`#`).
- The game ends when no more valid moves remain.

---

## Example Board

Before move:

```
  A B C D E F
1 _ _ _ _ _ _
2 _ _ _ _ _ _
3 _ _ _ _ _ _
4 _ _ _ _ _ _
5 _ _ _ _ _ _
6 _ _ _ _ _ _
```

After Player X places at C3:

```
  A B C D E F
1 _ _ _ _ _ _
2 _ # # # _ _
3 _ # X # _ _
4 _ # # # _ _
5 _ _ _ _ _ _
6 _ _ _ _ _ _
```

---

## Notes

- All user input is case-insensitive.
- Illegal moves prompt a retry.
- The last player to make a valid move wins the game.
