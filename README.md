# Connect Four - KI

This assignment is about a program that plays Connect Four (check https://en.wikipedia.org/wiki/Connect_Four or whatever source you like). 
Actually we obtained a Java code from 1999 which already uses MinMaxPlayer and some alpha-beta pruning. There are some flaws which we will improve. Moreover we will do some performance measurements.

## Quickstart

Prerequisites: 
- VS Code
- Docker
- VS Code Extension: Dev Containers
- X-Server installed and running on host machine
  - I use https://sourceforge.net/projects/vcxsrv/ on Windows 11

Compile and Run:
- Open this directory in VS Code DevContainers
- Press F5 to compile and run the applet
- You should see the applet in your running X-Server
- Happy developing 🧑‍💻

## Task 8

### 1. Suboptimal Evaluation Function

**The evaluation function getStrength(maxPlayer) could be a primary factor:**

  Victory Detection: If getStrength does not provide an appropriately high value for an immediate winning move (like setting to Integer.MAX_VALUE when 4InARow exists), the algorithm might not recognize the urgency or value of making that move.
    Scoring Nuances: The function might not adequately differentiate between nearly winning scenarios and other less advantageous ones. For instance, the difference in score between three in a row and four in a row might not be as significant as needed to always prioritize a win.

### 2. Alpha-Beta Pruning Effects

**In the expandMaxNode and expandMinNode methods, pruning decisions could prematurely cut off exploration of potentially winning moves:**

  Early Pruning: If a sibling node has set a high parentMinimum or low parentMaximum score, these thresholds might cause a winning move to be pruned away if it’s not explored early enough in the move list.
    Order of Exploration: The order in which moves are evaluated can significantly impact Alpha-Beta pruning. If winning moves are not among the first explored, the algorithm might settle on a suboptimal path due to the pruning of potentially better moves found later in the sequence.

### 3. Resource Constraints and Interruptions

**As seen in your code, if the computation exceeds certain time limits or if the execution thread is interrupted (Thread.currentThread().isInterrupted()), the algorithm may terminate early or not evaluate all possible moves:**

  Time and Computation Limits: Constraints on time and computational resources might prevent the algorithm from exploring all optimal moves, especially deeper in the move list.
    Thread Interruption: External interruptions could force an early return, possibly skipping the evaluation of a winning move.

### 4. Depth Limitation

**The depth parameter controls how many moves ahead the algorithm looks. If the depth is not sufficiently large:**

  Shallow Searches: In cases of shallow depth settings, crucial moves that would lead to a win in subsequent turns might be overlooked because the algorithm does not project far enough into the future to see the game's resolution.

### 5. Implementation Errors

**Bugs or logic errors in the implementation can lead to unexpected behaviors:**

  Misinterpretation of Game State: Errors in how moves and reversals (undoLastMove) are handled, or mistakes in updating or assessing game state (board.isGameOver()) could cause the algorithm to misjudge the value of certain positions.
