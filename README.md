# 🧩 Board Games in Python

This repository contains simple, text-based implementations of two classic board games — **Battleship** and **Obstruction** — built in Python as part of coursework for *Introduction to Computer Science (CS-UH 1001)* at NYU Abu Dhabi.

## 🎮 Included Games

### 🔹 Obstruction
A grid-based strategy game for 2–5 players. Players take turns placing their checkers, blocking adjacent cells. The last player able to move wins.

- Board: 2D grid (default: 6x6)
- Features: turn-based logic, dynamic board size, input validation

### 🔹 Battleship (1D)
A simplified one-dimensional version of Battleship where the player has 3 attempts to guess the location of a hidden 2-cell ship.

- Board: 1D list (default: 15 cells)
- Features: radar feedback on misses, random ship placement, limited turns

## 🚀 How to Run

```bash
python3 Obstruction.py
python3 Battleship.py
