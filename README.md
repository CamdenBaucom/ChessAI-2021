# Chess AI
## Planning
The goal of this project will be to create a basic chess artificial intelligence that can play against a human. Link a human brain, the ai will take inputs, the positions of the pieces, create evaluations, and output a response, the final move. Regarding the size of such a project, it is likely that the ai will only be able to play very basic chess and that a human player with any expreience should easily be able to crush it.  
### Initial Framework
The first problem is creating a chess board that follows the rules of the game. My plan is to use a 10x12 Mailbox, a square by square (as opposed to piece by piece) representation of the board that stores several values for all 64 squares of the board. At all times, each square must know both what the color of the piece is (black, white, or empty) and what type of piece it is (pawn, queen, rook, etc.). Additionally for certain pieces it must contain additional triggers, specifically for the king, rook, and pawn for their special moves. Instead of a traditional 8x8 board, the use of a 10x12 allows for an easy check to see whether a move goes off the board: if the value of a square is -1, a move their is invalid. Although most pieces could be at maximum one square of the side, creating a 9x9 board, knights on the edge can go two squares off the board, creating a 12x12 board. Finally, since these are all elements of an index, going right two squares next to the edge brings you to the left side of the board, eliminating the need for two values of -1 on both sides, leaving a 10x12 board.
```
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1,  0,  1,  2,  3,  4,  5,  6,  7, -1,
-1,  8,  9, 10, 11, 12, 13, 14, 15, -1,
-1, 16, 17, 18, 19, 20, 21, 22, 23, -1,
-1, 24, 25, 26, 27, 28, 29, 30, 31, -1,
-1, 32, 33, 34, 35, 36, 37, 38, 39, -1,
-1, 40, 41, 42, 43, 44, 45, 46, 47, -1,
-1, 48, 49, 50, 51, 52, 53, 54, 55, -1,
-1, 56, 57, 58, 59, 60, 61, 62, 63, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1
```
