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
To actually make moves the program checks full eligibility requirements, discussed later, then updates the value of the end position with the value of the starting position and the value of the starting position with 0. Additionally, the program stores the value of the end position before the new piece moved there and the very last starting and ending positions, as well as appending those last starting and ending positions into an array of all prior moves. Finally it changes the turn by flipping the value of the iswhitemove boolean state.
```ruby
def move(movestart,moveend):
	if (movestart in (in_check_eligible_move_start)) and (moveend in (in_check_eligible_move_end)):
		global last_piece_taken
		last_piece_taken = board64[moveend]
		board64[moveend] = board64[movestart]
		board64[movestart] = '0'
		print("Possible")
		global last_movestart
		last_movestart = movestart
		global last_moveend
		last_moveend = moveend
		global old_movestart
		old_movestart.append(movestart)
		global old_moveend
		old_moveend.append(moveend)
		global old_piece_taken
		old_piece_taken.append(last_piece_taken)
		global iswhitemove
		iswhitemove = not iswhitemove
	else:
		print("Not possible")
```
Accompanying move() are two other move functions with different eligibility requirements. The first of the two is test_move() which only checks basic eligibility is important in stopping potential feedback loops when calculating total eligibility. The other, force_move() has no requirements and accompanies two special moves, en passant and castling, that occur over two stages. 

Finally unmove() undoes a move by reversing the prior formula and using the stored value of the last piece taken. 
```ruby
def unmove():
	global last_movestart
	global last_moveend
	global last_piece_taken
	board64[last_movestart] = board64[last_moveend]
	board64[last_moveend] = last_piece_taken
	global iswhitemove
	iswhitemove = not iswhitemove
```
#### Basic Eligibility
The first layer of eligibility checks general rules, such as bishops moving diagonally or rooks moving horizontally and vertically. The central hub of sorts is move_is_legal(), which identifies what piece is moving and then checks the piece specific functions that determine eligibility.
```ruby
if board120[(move_convtr_64120(movestart))] in ('p','P'):
	return move_pawn_is_legal(movestart,moveend)
elif board120[(move_convtr_64120(movestart))] in ('r','R'):
	return move_rook_is_legal(movestart,moveend)
elif board120[(move_convtr_64120(movestart))] in ('n','N'):
	return move_knight_is_legal(movestart,moveend)
elif board120[(move_convtr_64120(movestart))] in ('b','B'):
	return move_bishop_is_legal(movestart,moveend)
elif board120[(move_convtr_64120(movestart))] in ('q','Q'):
	return move_queen_is_legal(movestart,moveend)
elif board120[(move_convtr_64120(movestart))] in ('k','K'):
	return move_king_is_legal(movestart,moveend)
else:
	return False
```
Pawns can only move in one direction depending on the piece color, or as is represented in the code, the letter case, and so for basic pawn eligibility, the movement direction is established first. From that, pawns can always move eight squares (in the right direction) if the end square is empty (represented by a value of 0 at the position). Additionally, pawns can move 16 squares if the end square is empty and their starting position is on their home row. Finally, pawns can take diagonally, 7 or 9 squares, if an enemy square occupies the position.
```ruby
if board120[(move_convtr_64120(movestart))] == 'p':
	pawn_move_direction = -1
else:
	pawn_move_direction = 1
```
```ruby
if movestart == moveend + (8*pawn_move_direction):
```
```ruby
elif (movestart == moveend + (16*pawn_move_direction)) and (((pawn_move_direction == -1) and (movestart in (8,9,10,11,12,13,14,15))) or ((pawn_move_direction == 1) and (movestart in (48,49,50,51,52,53,54,55)))):
```
```ruby
elif ((movestart == (moveend + 7*pawn_move_direction)) or (movestart == (moveend + 9*pawn_move_direction))) and board120[(move_convtr_64120(moveend))] in (can_take(movestart)) and board120[(move_convtr_64120(moveend))] != '0':
```
Rooks can move vertically, so in groups of 8 (8, 16, 24, etc.), and horizontally, so to any end square in their row. To calculate that I created a function, horiz_range() that took advantage of the ever useful floor division. 
```ruby
def move_rook_is_legal(movestart,moveend):
	if abs(movestart-moveend) in (8,16,24,32,40,48,56) and (hit_detec(movestart,moveend) == True) and (board120[(move_convtr_64120(moveend))] in (can_take(movestart))):
		return True
	elif moveend in horiz_range(movestart) and (hit_detec(movestart, moveend) == True) and (board120[(move_convtr_64120(moveend))] in (can_take(movestart))):
		return True
	else:
		return False
```
```ruby
def horiz_range(movestart):
	horiz_range_group_lower = movestart//8
	horiz_range_group_higher = horiz_range_group_lower+1
	return range(horiz_range_group_lower*8,horiz_range_group_higher*8)
```
Knights always move in distances of 6,10,15, or 17 squares, and so after passing the first condition (movement distance), I finally took advantage of the 120 square board. The only problem is that if I were to plug both the starting square and ending squares into the 64 to 120 square converter, it would skip over all the -1s and render the process useless. So, I plugged the starting value into the converter, and then made a math equation to convert the distance traveled on the 64 board to the equivalent distance traveled on the 120 square board. Then by combining the two, and plugging into the 120 square board, I could test the eligibility.
```ruby
def move_knight_is_legal(movestart,moveend):
	if (abs(movestart-moveend) in (6,10,15,17)) and (board120[(move_convtr_64120(moveend))] in (can_take(movestart))):
		move_knight_sign = -1*(abs(movestart-moveend)) / (movestart-moveend)
		move_knight_board120_check = ((move_convtr_64120(movestart)) + (((abs(movestart-moveend))+(((abs(movestart-moveend)) // 6) * 2))*move_knight_sign))
		move_knight_board120_check = int(move_knight_board120_check)
		if board120[move_knight_board120_check] not in ('-1'):
			return True
		else:
			return False
	else:
		return False
```
Bishops move in groups of 7 or 9 (7, 14, 21, etc. or 9, 18, 27, etc.). Queens, since they have the movement ability of both bishops and rooks, only have to have an eligible move inside of move_bishop_is_legal() or move_rook_is_legal(). 
```ruby
def move_bishop_is_legal(movestart,moveend):
	if abs(movestart-moveend) in (7,14,21,28,35,42,49,9,18,27,36,45,54,63) and (hit_detec(movestart,moveend) == True) and (board120[(move_convtr_64120(moveend))] in (can_take(movestart))):
```
```ruby
def move_queen_is_legal(movestart,moveend):
	if (move_bishop_is_legal(movestart,moveend) == True) or (move_rook_is_legal(movestart,moveend) == True):
```
Kings, with movement abilities of one square in any direction, can only move a distance of 1, 7, 8,  or 9. As an extra check, movement of 7, 8, or 9 are also checked through the 120 square board.
```ruby
def move_king_is_legal(movestart,moveend):
	if abs(movestart-moveend) in (1,7,8,9):
		move_king_sign = -abs(movestart-moveend) / (movestart-moveend)
		move_king_diff = abs(movestart-moveend)
		move_king_sign = int(move_king_sign)
		move_king_diff = int(move_king_diff)
		if abs(movestart-moveend) in (7,8,9):
			move_king_diff += 2
		if board120[(move_convtr_64120(movestart))+(move_king_diff*move_king_sign)] in (can_take(movestart)):
			return True
		else:
			return False
```
For all the previously mentioned movements, an ending square is eligible if it is either empty or occupied by an enemy piece. So, the simple function, can_take(), returns an array for which the value of the end position must be in.
```ruby
def can_take(movestart):
	if board120[(move_convtr_64120(movestart))].islower() == True:
		return ['P','R','N','B','Q','K','0']
	else:
		return ['p','r','n','b','q','k','0']
```
Finally, when a piece moves more than one square in any direction, I had to make sure that there was no piece in between the starting square and ending square. To do this I created a function called hit_detec(), with specific tests for horizontal, vertical, and diagonal movement. For each, I made a range of how many squares it moved, and then checked the in between squares on the 120 square board. For the diagonal movement, I was encountering problems so I tweaked just that one, so that it also checks the final ending position on the 120 square board.
```ruby
def hit_detec(movestart,moveend):
	hit_detec_sign = (moveend-movestart) / abs(moveend-movestart)
	hit_detec_sign = int(hit_detec_sign)
	if abs(movestart-moveend) in (8,16,24,32,40,48,56,64):
		hit_detec_vert_counter = abs(((movestart-moveend) / 8))
		hit_detec_vert_counter = int(hit_detec_vert_counter)
		hit_detec_vert_bool = False
		for i in range(hit_detec_vert_counter):
			hit_detec_vert_between = i*8
			if hit_detec_vert_between == 0:
				hit_detec_vert_bool = True
			elif board120[(move_convtr_64120(movestart+(hit_detec_sign*hit_detec_vert_between)))] == '0':
				hit_detec_vert_bool = True
			else:
				hit_detec_vert_bool = False
				return hit_detec_vert_bool
		return hit_detec_vert_bool
	elif moveend in horiz_range(movestart):
		hit_detec_horiz_counter = abs(movestart-moveend)
		hit_detec_horiz_counter = int(hit_detec_horiz_counter)
		hit_detec_horiz_bool = False
		for i in range(hit_detec_horiz_counter):
			if i == 0:
				hit_detec_horiz_bool = True
			elif board120[(move_convtr_64120(movestart+(hit_detec_sign*i)))] == '0':
				hit_detec_horiz_bool = True
			else:
				hit_detec_horiz_bool = False
				return hit_detec_horiz_bool
		return hit_detec_horiz_bool
	else:
		if abs(movestart-moveend) in (7,14,21,28,35,42,49):
			hit_detec_diag_counter = abs(((movestart-moveend) / 7))
			hit_detec_diag_inc = 9
		else:
			hit_detec_diag_counter = abs(((movestart-moveend) / 9))
			hit_detec_diag_inc = 11
		hit_detec_diag_counter = int(hit_detec_diag_counter)
		hit_detec_diag_bool = False
		for i in range(hit_detec_diag_counter):
			hit_detec_diag_between = i*hit_detec_diag_inc
			if hit_detec_diag_between == 0:
				hit_detec_diag_bool = True
			elif board120[(move_convtr_64120(movestart))+(hit_detec_sign*hit_detec_diag_between)] == '0':
				hit_detec_diag_bool = True
				if (i+1 == hit_detec_diag_counter):
					hit_detec_diag_between += hit_detec_diag_inc
					if board120[(move_convtr_64120(movestart))+(hit_detec_sign*hit_detec_diag_between)] in (can_take(movestart)):
						hit_detec_diag_bool = True
					else:
						hit_detec_diag_bool = False
						return hit_detec_diag_bool
			else:
				hit_detec_diag_bool = False
				return hit_detec_diag_bool
		return hit_detec_diag_bool
```

#### Specialized Eligibility



#### Total Eligibility



#### The Game


### Mistakes
Min/Max, board120 vs board64, counting 0 or not
### Overview
Blah Blah Blah
