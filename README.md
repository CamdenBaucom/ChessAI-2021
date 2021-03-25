# Chess AI
## Planning
The goal of this project will be to create a basic chess artificial intelligence that can play against a human. Link a human brain, the ai will take inputs, the positions of the pieces, create evaluations, and output a response, the final move. Regarding the size of such a project, it is likely that the ai will only be able to play very basic chess and that a human player with any expreience should easily be able to crush it.  
### Initial Framework
The first problem is creating a chess board that follows the rules of the game. My plan is to use a 10x12 Mailbox, a square by square (as opposed to piece by piece) representation of the board that stores several values for all 64 squares of the board. At all times, each square must know both what the color of the piece is (black, white, or empty) and what type of piece it is (pawn, queen, rook, etc.). Additionally for certain pieces it must contain additional triggers, specifically for the king, rook, and pawn for their special moves. Instead of a traditional 8x8 board, the use of a 10x12 allows for an easy check to see whether a move goes off the board: if the value of a square is -1, a move their is invalid. Although most pieces could be at maximum one square off the side, creating a 9x9 board, knights on the edge can go two squares off the board, creating a 12x12 board. Finally, since these are all elements of an index, going right two squares next to the edge brings you to the left side of the board, eliminating the need for two values of -1 on both sides, leaving a 10x12 board.
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


### Board Evaluation
The starting board evalutaion will be incredibly simple, just assign values to the pieces and count up the values on both sides. At this point the superiority of a computer becomes apparent when I ask it to go through all possible moves and determine the move which gives the computer the best value regardless of the opponents move. To accomplish I will implement something called Minimax which evaluates the computers best move, max, and the opponents worst move, min. It then moves through a depth first search, which evaluates one line all the way to the given depth before moving to sibling nodes. Once all sibling nodes are investigated it goes back up one level, moves to a sibling and back down to the given depth.
```
Depth:1                        (1)
Depth:2           (2)                       (9) 
Depth:3     (3)         (6)           (10)       (13)
Depth:4  (4)   (5)   (7)   (8)     (11)  (12) (14)  (15)
```
Essentially, the idea is that the computer chooses random moves for both sides going to the end depth and evalutes the position for both sides assigning a min (for opponent) and max (for computer) value. Additionally, since both values can be negative or positive, to show who is ahead, the overall value is the sum of the min and max. The computer then looks at the sibling nodes and evaluates the min or max value for that position and if that value is greater than the previous value, the min/max is updated, since the computer always assumes that the best move will be played. Once all siblings have been evaluated the computer moves back to a parent's siling and their children, updating min/max only at end nodes. When ever a position updatese the min/max value its path is stored so that if it is the best overall the computer can execute it. An easy improvement to this system is caled Alpha-Beta Pruning, which just allow the compter to stop looking at other siblings once one has been determined to have a worse min/max (or Alpha/Beta). For example, if a computer move has a best response of being up a queen, but a different computer move has one response of being down a queen, there is no need to look at all the other opponent responses since at least one is worse for the computer, thus greatly reducing the number of variants that must be searched and evaluated.

Zorbist Hasing - Transposition

