## Towers of Hanoi

This is a Python terminal game implementing the Towers of Hanoi puzzle.
I saw this when looking over the Codecademy course syllabus for DSA. I thought it looked interesting, so I decided to implement it with some extra features, such as:
   - input validation,
   - outputting the move counter when playing, whilst comparing it to the most optimal move amount,
   - clear invalid input messages.

It has been good practice using stacks :).


## How to Play

1. The game starts with all disks on the **Left Stack**, arranged from largest at the bottom to smallest at the top.
2. Your goal is to move all disks to the **Right Stack** following these rules:
   - Only one disk can be moved at a time.
   - You can only move the top disk from a stack.
   - No disk may be placed on top of a smaller disk.

3. The program will track the number of moves you make, and you can try to solve it in the **minimum number of moves**.


## Installation

**Option 1 — Download ZIP**
1. Click the green **Code** button
2. Select **Download ZIP** and extract it
3. Open in your IDE and run

**Option 2 — Clone using Git**
```bash
git clone https://github.com/samjj05/towers_of_hanoi.git
cd towers_of_hanoi
