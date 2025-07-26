
# Obstruction



A Python implementation of the classic paper-and-pencil game Obstruction, developed as part of the Introduction to Computer Science (CS-UH 1001) course at NYU Abu Dhabi in Spring 2024

🎯 Objective

Obstruction is a turn-based, two-player game played on a 2D grid. Players alternate placing their checkers (X, O, etc.) on unoccupied spaces. After a move, all adjacent cells are "blocked" (marked with #). The player unable to make a move loses the game.

🧩 Features

- Fully text-based interface in the terminal.
- Supports dynamic board sizes (default: 6x6).
- Configurable number of players (up to 5).
- Uses clear, modular functions for:
  - Input validation
  - Move handling
  - Board display
  - Neighbor blocking
- Randomized first player selection.
- Game ends when no more legal moves are possible.

📦 Files

- Obstruction.py: Main source code file containing the game logic.

🚀 Getting Started

Prerequisites

- Python 3.x
- Unix/Linux terminal (recommended)

Running the Game

1. Open a terminal.
2. Navigate to the directory containing the script.
3. Run: python3 Obstruction.py

Controls

- Players take turns entering a coordinate like C3 (column letter followed by row number).
- Invalid or occupied inputs prompt an error message and retry.

🛠️ Configuration

To change the board or player settings, modify the following constants at the top of Obstruction.py:

NUM_ROW = 6
NUM_COL = 6
NUM_PLAYERS = 2

- Maximum board size: 9x9
- Minimum board size: 4x4
- Maximum players: 5 (checkers are ['X','O','M','N','P'])

📝 Assignment Highlights

This project demonstrates core concepts in Python:

- Working with lists and loops
- String manipulation
- Conditional logic
- Game state management
- Modular programming

