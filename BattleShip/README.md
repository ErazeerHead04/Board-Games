# Battleship Game (1D Version)

A simplified, one-dimensional implementation of the classic Battleship game in Python. This terminal-based game challenges the player to locate and sink a hidden two-cell ship within three attempts.

---

## Objective

The player attempts to sink a randomly placed 2-cell ship on a one-dimensional board by guessing positions using letter-based input. The game provides feedback on hits, misses, and near-misses ("radar" guidance). The player has three attempts to succeed.

---

## Features

- 1D board with a default length of 15 (customizable).
- Ship of length 2 is randomly placed and hidden from the player.
- User inputs a single letter per attempt (e.g., `C`).
- Feedback includes:
  - `O`: Hit (part of ship found)
  - `X`: Miss (with distance feedback)
- Invalid input prompts retry.
- Game ends when the ship is sunk or attempts are exhausted.
- Fully text-based interface in the terminal.

---

## Game Setup

- **Board Size**: Default is 15  
- **Ship Length**: 2  
- **Attempts**: 3  

The board is represented as a one-dimensional list of spaces `" "`, labeled `A` to `O`.

Ship placement logic:

```python
import random
random.randint(0, BOARD_SIZE - SHIP_LENGTH)
```

---

## How to Run

1. Open your terminal.
2. Navigate to the folder containing the script.
3. Run the following command:

```bash
python3 battleship.py
```

---

## Game Flow Example

**Initial Board:**

```
A B C D E F G H I J K L M N O
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _
```

**Player Guess: `E`**

- If it's a hit → mark with `O`
- If it's a miss → mark with `X`, and show how far it is from the ship
- Continue until ship is sunk or attempts run out

---

## Customization

Modify the following constants at the top of the script to adjust game settings:

```python
BOARD_SIZE = 15
SHIP_LENGTH = 2
MAX_ATTEMPTS = 3
```

You can increase the board length, change the ship size, or allow more attempts for easier or harder gameplay.
