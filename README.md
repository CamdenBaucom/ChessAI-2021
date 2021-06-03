# Chess AI
## Planning
The goal of this project will be to create a basic chess artificial intelligence that can play against a human. Link a human brain, the AI will take inputs, the positions of the pieces, create evaluations, and output a response, the final move. Regarding the size of such a project, it is likely that the AI will only be able to play very basic chess and that a human player with any experience should easily be able to crush it.  
### Initial Framework
The first problem is creating a chess board that follows the rules of the game. My plan is to use a 10x12 Mailbox, a square by square (as opposed to piece by piece) representation of the board that stores several values for all 64 squares of the board. At all times, each square must know both what the color of the piece is (black, white, or empty) and what type of piece it is (pawn, queen, rook, etc.). Additionally for certain pieces it must contain additional triggers, specifically for the king, rook, and pawn for their special moves. Instead of a traditional 8x8 board, the use of a 10x12 allows for an easy check to see whether a move goes off the board: if the value of a square is -1, a move there is invalid. Although most pieces could be at maximum one square off the side, creating a 9x9 board, knights on the edge can go two squares off the board, creating a 12x12 board. Finally, since these are all elements of an index, going right two squares next to the edge brings you to the left side of the board, eliminating the need for two values of -1 on both sides, leaving a 10x12 board.
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
The starting board evaluation will be incredibly simple, just assign values to the pieces and count up the values on both sides. At this point the superiority of a computer becomes apparent when I ask it to go through all possible moves and determine the move which gives the computer the best value regardless of the opponent's move. To accomplish this I will implement something called Minimax which evaluates the computer's best move, max, and the opponent's worst move, min. It then moves through a depth first search, which evaluates one line all the way to the given depth before moving to sibling nodes. Once all sibling nodes are investigated it goes back up one level, moves to a sibling and back down to the given depth.
```
Depth:1                        (1)
Depth:2           (2)                       (9) 
Depth:3     (3)         (6)           (10)       (13)
Depth:4  (4)   (5)   (7)   (8)     (11)  (12) (14)  (15)
```
Essentially, the idea is that the computer chooses random moves for both sides going to the end depth and evaluates the position for both sides, assigning a min (for opponent) and max (for computer) value. Additionally, since both values can be negative or positive, to show who is ahead, the overall value is the sum of the min and max. The computer then looks at the sibling nodes and evaluates the min or max value for that position and if that value is greater than the previous value, the min/max is updated, since the computer always assumes that the best move will be played. Once all siblings have been evaluated the computer moves back to a parent's sibling and their children, updating min/max only at end nodes. Whenever a position updates the min/max value its path is stored so that if it is the best overall the computer can execute it. An easy improvement to this system is called Alpha-Beta Pruning, which just allows the computer to stop looking at other siblings once one has been determined to have a worse min/max (or Alpha/Beta). For example, if a computer move has a best response of being up a queen, but a different computer move has one response of being down a queen, there is no need to look at all the other opponent responses since at least one is worse for the computer, thus greatly reducing the number of variants that must be searched and evaluated.

### Advanced Additions
If there is enough time, I hope to implement two systems that will greatly increase the computer's level of play. First is an opening book, which stores commonly used and studied game opening which the computer chooses randomly from to start the game. This eliminates early game move searching and evaluating, speeding up the game and making each move unique. The second is an Endgame book, which stores common endgames with known outcomes and searches the board to see if they are applicable.

### Timeline
- [X] April 16: Working on basic rules 
- [X] April 23: Working on basic rules
- [X] April 30: Working on basic rules
- [X] May 7: Working on basic rules
- [X] May 14: Working on basic rules
- [X] May 21: Done with basic rules
- [X] May 28: Working on Min/Max Alpha/Beta
- [ ] June 4: Done with Min/Max Alpha/Beta

## Reality
Eight weeks and 800 lines of code later, the project is complete. It allows the user to play a full game of chess against another user or against a computer playing random moves. Upon starting the code, it quickly became apparent that the size of the project was even greater than I had earlier anticipated. The code itself is really composed of 33 functions whose uses range from graphical to backend to functional. To determine eligibility, I first had to calculate general, then specialized, then total moves, all of which needed to reference each but had to be clearly separated so as to not enter into a feedback loop. In order to test moves, moves had to be done and undone, all while incorporating special moves that simply did not want to cooperate. In the end, it was not my code, but logic failings that stopped me short from completing my total goal. Nevertheless, I am extremely proud of my time and effort invested, and the creation of a project that would have seemed unimaginable at the beginning of the year.
### Code Analysis
The code is a behemoth, and explaining each line and choice would be a project in and of itself, but I’ll do my best to explain the major components and sections. 
#### The Board
As mentioned in the planning, I created a 120 square board and a 64 square board, the former to make eligibility requirements easier and the latter to make movement requests easier. For the 120 square board, it allowed me to not worry about crazy moves wrapping around the board as demonstrated in the example below.  If we imagine index 44 was a pawn, we know that pawns can take other pieces diagonally, and so if there was an enemy piece on index 35 or 37, the pawn could take it. This means the code must check eligibility at an index of a distance of 7 and 9 from the starting square (44-35 = 9 and 44-37 = 7). However, if the same logic was applied to index 48, on the 64 square board, it would check 41 and 39, even though 39 is actually on the opposite side of the board. But, doing the same on the 120 square board (checking an index of a distance of 7 and 9* from the starting square), we see that we only have 41 and -1, and the -1 can then be ignored.  The 64 square board is easier, however, when turning movement requests into reality. This is because the user will be seeing a 64 square board and submitting requests in terms of that board, thus by using that board in the backend, I will reduce the amount of conversion that needs to happen. 

*As a side note, since the 120 square board is wider than the 64 square board, the code really checks a distance of 9 and 11 from the starting square
```
120 Square Board
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

64 Square Board
0,  1,  2,  3,  4,  5,  6,  7,
8,  9, 10, 11, 12, 13, 14, 15,
16, 17, 18, 19, 20, 21, 22, 23,
24, 25, 26, 27, 28, 29, 30, 31,
32, 33, 34, 35, 36, 37, 38, 39,
40, 41, 42, 43, 44, 45, 46, 47,
48, 49, 50, 51, 52, 53, 54, 55,
56, 57, 58, 59, 60, 61, 62, 63
```

In terms of actually displaying the board, which as recently mentioned would just be the 64 board, a couple problems had to be solved. Firstly, since the board was an array, if you print it out on its own, it just shows one long line of array elements, without any line skipping. To solve this, I had to turn the array into a string, while inserting newline commands (“\n”) between every eight indexes. To do this, I created an eight element range (8*8 = 64 and a full board) which turned into two variables that were the first and last index of that line on the board. For example, if z was 4, then x would be 32, and y would be 24, corresponding to the fourth row as seen on the 64 square board. But wait a minute, the 24 corresponds correctly, but the 32 is one greater than the 31 seen on the board. This works because the range function starts at its first parameter and goes up to, but does not reach, its last parameters, meaning that the “for z in range(1,9):” would loop through, with values of z at 1,2,3,4,5,6,7, and 8. Now that I have a variable i for which I can access the elements of each board row (0-7, then 8-15, then 16-23, etc.), I can take the individual value of the board at those elements and put it into a string that nicely formats the values into little boxes. Each row is then attached a newline command (“\n”), with the next row added on at the end, due to the string's ability to essentially append themselves with a simple +. With that sorted, the second problem is formatting the board so that the player can easily see where rows 1-8 and columns a-h are, as that is standard chess notation. Since I already had values in groups of 8, I took advantage of something called floor division, which finds the largest integer quotient whose product with the divisor does not exceed the dividend, in other words the quotient rounded down without any remainder. This gave me one number for each group which I printed in front of each row. Then at the end, I simply added another sting with the letters a-h aligned with each column.

```ruby
for z in range(1,9):
	y = (z-1)*8
	x = z*8
	for i in range(y,x):
		board64short.append(board64[i])
		boardnumbers = 8 - ((i // 8) )
		stri = str(boardnumbers)
		boardstrstart = stri + " [ "
		boardstrend = " ]"
		boardstrmid = ' ][ '.join(map(str, board64short))
	boardstrnew = ""
	boardstrnew = boardstrstart+boardstrmid+boardstrend+"\n"
	global boardstr
	boardstr = boardstr+boardstrnew
	board64short.clear()
boardstr = boardstr + "    a    b    c    d    e    f    g    h"
print(boardstr)
```

```
Full Board with numbers
8 [ 0 ][ 1 ][ 2 ][ 3 ][ 4 ][ 5 ][ 6 ][ 7 ]
7 [ 8 ][ 9 ][ 10 ][ 11 ][ 12 ][ 13 ][ 14 ][ 15 ]
6 [ 16 ][ 17 ][ 18 ][ 19 ][ 20 ][ 21 ][ 22 ][ 23 ]
5 [ 24 ][ 25 ][ 26 ][ 27 ][ 28 ][ 29 ][ 30 ][ 31 ]
4 [ 32 ][ 33 ][ 34 ][ 35 ][ 36 ][ 37 ][ 38 ][ 39 ]
3 [ 40 ][ 41 ][ 42 ][ 43 ][ 44 ][ 45 ][ 46 ][ 47 ]
2 [ 48 ][ 49 ][ 50 ][ 51 ][ 52 ][ 53 ][ 54 ][ 55 ]
1 [ 56 ][ 57 ][ 58 ][ 59 ][ 60 ][ 61 ][ 62 ][ 63 ]
    a    b    c    d    e    f    g    h    

Full Board
8 [ r ][ n ][ b ][ q ][ k ][ b ][ n ][ r ]
7 [ p ][ p ][ p ][ p ][ p ][ p ][ p ][ p ]
6 [ 0 ][ 0 ][ 0 ][ 0 ][ 0 ][ 0 ][ 0 ][ 0 ]
5 [ 0 ][ 0 ][ 0 ][ 0 ][ 0 ][ 0 ][ 0 ][ 0 ]
4 [ 0 ][ 0 ][ 0 ][ 0 ][ 0 ][ 0 ][ 0 ][ 0 ]
3 [ 0 ][ 0 ][ 0 ][ 0 ][ 0 ][ 0 ][ 0 ][ 0 ]
2 [ P ][ P ][ P ][ P ][ P ][ P ][ P ][ P ]
1 [ R ][ N ][ B ][ Q ][ K ][ B ][ N ][ R ]
    a    b    c    d    e    f    g    h     
```

#### Backend Conversions
Since the program would be running off the 120 square and 64 square boards at different points, I needed a way to independently update the value of one on to the other, so I created two functions to update the value of 64 with 120, and 120 with 64.  To do this I used the enumerate() function which outputs two things at each index: the index number, and the value at that index. So in the code below, index is the index number, and sqr is the value at that index of board120. Then looping through all indexes and values of board120, if the value was not -1, it would be pushed to the 64 square board.

```ruby
def upd_board_12064():
	for index, sqr in enumerate(board120):
		if not (sqr == '-1'):
			global updboardcounter12064
			board64[updboardcounter12064] = board120[index]
			updboardcounter12064 += 1
	updboardcounter12064 = 0
```

With that complete, the only other big conversion problem between the boards was converting board positions on the 64 square board, where inputs would arrive, to the 120 square board, through which the inputs needed to go. I spent a lot of time on a convoluted system of calculating the values, before eventually realizing that all I needed to do was find out how many times the 64 square board position went onto a new row, again done by floor division, and multiply that by two (to simulate the two -1 values in between each row on the 120 square board) and then add that with 21 (the number of -1 values before everything else on the 120 square board) and the original position. 

```ruby
def move_convtr_64120(movestart):
	move_convtr_64120_var1 = movestart // 8
	move_convtr_64120_var1 = int(move_convtr_64120_var1)
	movestart = movestart + (2*move_convtr_64120_var1) + 21
	return movestart
```
The final piece in the conversion puzzle was converting the chess notation that players put in (A3, D6, H7, etc.) into the corresponding index on the 64 square board so that the computer could understand the move. To do this, I essentially just turned each letter of the input into an index in an array, and I searched that array for values to update the numerical position.

```ruby
board_notation_char = [char for char in movestart]
```

#### Movement



#### Basic Eligibility



#### Specialized Eligibility



#### Total Eligibility



#### The Game


### Mistakes
Min/Max, board120 vs board64, counting 0 or not
### Overview
Blah Blah Blah
