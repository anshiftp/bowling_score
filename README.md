# Ten-Pin Bowling Score Calculator (Python)

## Overview
This project calculates the total score of a single ten-pin bowling game using Python.  
The game is provided as a string input, and the program computes the final score based on standard bowling rules.

---

## Rules Summary
- A game has **10 frames**
- Frames 1–9 allow up to two rolls
- Frame 10 may have a third roll if a strike or spare is scored

### Scoring
- **Open frame**: Sum of pins
- **Spare (/)**: 10 + next roll
- **Strike (X)**: 10 + next two rolls

---

## Input Format
- `0–9` → pins knocked down  
- `X` → strike  
- `/` → spare  
- `-` → miss  

### Examples
- `9-9-9-9-9-9-9-9-9-9-` → 90  
- `XXXXXXXXXXXX` → 300  
- `5/5/5/5/5/5/5/5/5/5/5` → 150  

---

## Project Structure
.
├── bowling_score.py
├── test_bowling_score.py
├── README.md
└── ERP_Presentation.pptx


## How to Run
```bash
python test_bowling_score.py

Testing
Basic test cases are included using Python assert statements to validate common scenarios like strikes, spares, and open frames.

Author
Anshif Thekkumpurath



Copy code
