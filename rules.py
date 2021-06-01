board120 = ['-1','-1','-1','-1','-1','-1','-1','-1','-1','-1',
'-1','-1','-1','-1','-1','-1','-1','-1','-1','-1',
'-1','r','n','b','q','k','b','n','r','-1',
'-1','p','p','p','p','p','p','p','p','-1',
'-1','0','0','0','0','0','0','0','0','-1',
'-1','0','0','0','0','0','0','0','0','-1',
'-1','0','0','0','0','0','0','0','0','-1',
'-1','0','0','0','0','0','0','0','0','-1',
'-1','P','P','P','P','P','P','P','P','-1',
'-1','R','N','B','Q','K','B','N','R','-1',
'-1','-1','-1','-1','-1','-1','-1','-1','-1','-1',
'-1','-1','-1','-1','-1','-1','-1','-1','-1','-1']

board64 = [ '0','1','2','3','4','5','6','7',
'8','9','10','11','12','13','14','15',
'16','17','18','19','20','21','22','23',
'24','25','26','27','28','29','30','31',
'32','33','34','35','36','37','38','39',
'40','41','42','43','44','45','46','47',
'48','49','50','51','52','53','54','55',
'56','57','58','59','60','61','62','63']

iswhitemove = True

board64short = []
boardstr = ""

def show_board():
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
	boardstrmid = ""
	boardstrnew = ""
	boardstr = ""
	board64short.clear()

updboardcounter12064 = 0
updboardcounter64120 = 0

def upd_board_12064():
	for index, sqr in enumerate(board120):
		if not (sqr == '-1'):
			global updboardcounter12064
			board64[updboardcounter12064] = board120[index]
			updboardcounter12064 += 1
	updboardcounter12064 = 0

def upd_board_64120():
	for index, sqr in enumerate(board120):
		if not (sqr == '-1'):
			global updboardcounter64120
			board120[index] = board64[updboardcounter64120]
			updboardcounter64120 += 1
	updboardcounter64120 = 0

def move_convtr_64120(movestart):
	move_convtr_64120_var1 = movestart // 8
	move_convtr_64120_var1 = int(move_convtr_64120_var1)
	movestart = movestart + (2*move_convtr_64120_var1) + 21
	return movestart

def horiz_range(movestart):
	horiz_range_group_lower = movestart//8
	horiz_range_group_higher = horiz_range_group_lower+1
	return range(horiz_range_group_lower*8,horiz_range_group_higher*8)

def board_notation_convtr(movestart):
	board_notation_char = [char for char in movestart]
	if 'a' in board_notation_char or 'A' in board_notation_char:
		board_notation_counter = 7
	elif 'b' in board_notation_char or 'B' in board_notation_char:
		board_notation_counter = 6
	elif 'c' in board_notation_char or 'C' in board_notation_char:
		board_notation_counter = 5
	elif 'd' in board_notation_char or 'D' in board_notation_char:
		board_notation_counter = 4
	elif 'e' in board_notation_char or 'E' in board_notation_char:
		board_notation_counter = 3
	elif 'f' in board_notation_char or 'F' in board_notation_char:
		board_notation_counter = 2
	elif 'g' in board_notation_char or 'G' in board_notation_char:
		board_notation_counter = 1
	elif 'h' in board_notation_char or 'H' in board_notation_char:
		board_notation_counter = 0
	else:
		return False
	if '1' in board_notation_char:
		board_notation_counter += 0
	elif '2' in board_notation_char:
		board_notation_counter += 8
	elif '3' in board_notation_char:
		board_notation_counter += 16
	elif '4' in board_notation_char:
		board_notation_counter += 24
	elif '5' in board_notation_char:
		board_notation_counter += 32
	elif '6' in board_notation_char:
		board_notation_counter += 40
	elif '7' in board_notation_char:
		board_notation_counter += 48
	elif '8' in board_notation_char:
		board_notation_counter += 56
	else:
		return False
	board_notation_counter = 63-board_notation_counter
	return board_notation_counter

def can_take(movestart):
	if board120[(move_convtr_64120(movestart))].islower() == True:
		return ['P','R','N','B','Q','K','0']
	else:
		return ['p','r','n','b','q','k','0']

last_movestart = 0
last_moveend = 0
last_piece_taken = ''
old_movestart = []
old_moveend = []
old_piece_taken = []

def test_move(movestart,moveend):
	if move_is_legal(movestart,moveend) == True:
		global last_piece_taken
		last_piece_taken = board64[moveend]
		board64[moveend] = board64[movestart]
		board64[movestart] = '0'
		global last_movestart
		last_movestart = movestart
		global last_moveend
		last_moveend = moveend
		global iswhitemove
		iswhitemove = not iswhitemove
		return True
	else:
		print("Not possible")
		return False

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

def force_move(movestart,moveend):
	global last_piece_taken
	last_piece_taken = board64[moveend]
	board64[moveend] = board64[movestart]
	board64[movestart] = '0'
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

def unmove():
	global last_movestart
	global last_moveend
	global last_piece_taken
	board64[last_movestart] = board64[last_moveend]
	board64[last_moveend] = last_piece_taken
	global iswhitemove
	iswhitemove = not iswhitemove

def unmove_depth(depth):
	global old_movestart
	global old_moveend
	global old_piece_taken

#
#
#
#
#
#Need to Work on this
#
#
#
#
#

def move_is_legal(movestart,moveend):
	if (movestart != moveend) and (iswhitemove == True and (board120[(move_convtr_64120(movestart))] in ('P','R','N','B','Q','K'))) or (iswhitemove == False and (board120[(move_convtr_64120(movestart))] in ('p','r','n','b','q','k'))):
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
	else:
		return False


def move_pawn_is_legal(movestart,moveend):
	if board120[(move_convtr_64120(movestart))] == 'p':
		pawn_move_direction = -1
	else:
		pawn_move_direction = 1
	if movestart == moveend + (8*pawn_move_direction):
		if board120[(move_convtr_64120(moveend))] == '0':
			return True
		else:
			return False
	elif (movestart == moveend + (16*pawn_move_direction)) and (((pawn_move_direction == -1) and (movestart in (8,9,10,11,12,13,14,15))) or ((pawn_move_direction == 1) and (movestart in (48,49,50,51,52,53,54,55)))):
		if (hit_detec(movestart,moveend) == True) and (board120[move_convtr_64120(moveend)] == '0'):
			return True
		else:
			return False
	elif ((movestart == (moveend + 7*pawn_move_direction)) or (movestart == (moveend + 9*pawn_move_direction))) and board120[(move_convtr_64120(moveend))] in (can_take(movestart)) and board120[(move_convtr_64120(moveend))] != '0':
		if movestart not in (8,16,24,32,40,48,15,23,31,39,47,55):
			return True
		elif movestart == moveend + 7*pawn_move_direction and ((pawn_move_direction == -1 and movestart in (15,23,31,39,47,55)) or (pawn_move_direction == 1 and movestart in (8,16,24,32,40,48))):
			return True
		elif movestart == moveend + 9*pawn_move_direction and ((pawn_move_direction == -1 and movestart in (8,16,24,32,40,48)) or (pawn_move_direction == 1 and movestart in (15,23,31,39,47,55))):
			return True
		else:
			return False
	elif (len(old_movestart) > 0) and (((old_movestart[-1])-(old_moveend[-1])) == (-16*pawn_move_direction)):
		if (board120[move_convtr_64120(old_moveend[-1])] in ('p','P')) and (((old_moveend[-1]) - (8*pawn_move_direction)) == (moveend)):
			if ((board120[(move_convtr_64120(movestart)) + 1]) == (board120[move_convtr_64120(old_moveend[-1])])):
				if (pawn_move_direction == -1) and ((movestart-moveend) == (9*pawn_move_direction)):
					return True
				elif (pawn_move_direction == 1) and ((movestart-moveend) == (7*pawn_move_direction)):
					return True
				elif ((board120[(move_convtr_64120(movestart)) - 1]) == (board120[move_convtr_64120(old_moveend[-1])])):
					if (pawn_move_direction == -1) and ((movestart-moveend) == (7*pawn_move_direction)):
						return True
					elif (pawn_move_direction == 1) and ((movestart-moveend) == (9*pawn_move_direction)):
						return True
					else:
						return False
				else:
					return False
			elif ((board120[(move_convtr_64120(movestart)) - 1]) == (board120[move_convtr_64120(old_moveend[-1])])):
				if (pawn_move_direction == -1) and ((movestart-moveend) == (7*pawn_move_direction)):
					return True
				elif (pawn_move_direction == 1) and ((movestart-moveend) == (9*pawn_move_direction)):
					return True
				else:
					return False
			else:
				return False
	else:
		return False

def en_passant():
	global last_piece_taken
	global old_movestart
	global old_moveend
	global en_passant_unmove_state
	en_passant_unmove_state = False
	if (len(old_movestart) > 0) and (last_piece_taken == '0') and (abs(old_movestart[-1]-old_moveend[-1]) in (7,9)) and (board120[move_convtr_64120(old_moveend[-1])] in ('p','P')):
		if board120[move_convtr_64120(old_moveend[-1])] == 'p':
			last_piece_taken = 'P'
			board64[last_moveend - 8] = '0'
			en_passant_unmove_state = True
		else:
			last_piece_taken = 'p'
			board64[last_moveend + 8] = '0'
			en_passant_unmove_state = True

def pawn_promotion():
	global old_moveend
	global pawn_promotion_unmove_state
	global pawn_promotion_unmove_old_value
	pawn_promotion_unmove_state = False
	pawn_promotion_unmove_old_value = ''
	new_piece_input_works = False
	if (len(old_moveend) > 0) and (old_moveend[-1] in (0,1,2,3,4,5,6,7,56,57,58,59,60,61,62,63)) and (board120[move_convtr_64120(old_moveend[-1])] in ('p','P')):
		pawn_promotion_unmove_old_value = board120[move_convtr_64120(old_moveend[-1])]
		pawn_promotion_unmove_state = True
		if (one_player == True) and (iswhitemove != comp_goes_first):
			if (old_moveend[-1] in (0,1,2,3,4,5,6,7)):
				new_piece = "Q"
			else:
				new_piece = 'q'
		else:
			while new_piece_input_works == False:
				new_piece_input = input("Type what piece you want to promote your pawn to:\n")
				if (old_moveend[-1] in (0,1,2,3,4,5,6,7)):
					if new_piece_input in ("Knight","knight","N","n","Night","night","Nite","nite","Horse","horse"):
						new_piece = "N"
						new_piece_input_works = True
					elif new_piece_input in ("Rook","rook","R","r","Rock","rock","Rok","rok","Castle","castle","Tower","tower"):
						new_piece = "R"
						new_piece_input_works = True
					elif new_piece_input in ("Bishop","bishop","B","b","Priest","priest"):
						new_piece = "B"
						new_piece_input_works = True
					elif new_piece_input in ("Queen","queen","Q","q"):
						new_piece = "Q"
						new_piece_input_works = True
					else:
						print("Please type a valid piece (Kings and Pawns are not allowed)")
				else:
					if new_piece_input in ("Knight","knight","N","n","Night","night","Nite","nite","Horse","horse"):
						new_piece = "n"
						new_piece_input_works = True
					elif new_piece_input in ("Rook","rook","R","r","Rock","rock","Rok","rok","Castle","castle","Tower","tower"):
						new_piece = "r"
						new_piece_input_works = True
					elif new_piece_input in ("Bishop","bishop","B","b","Priest","priest"):
						new_piece = "b"
						new_piece_input_works = True
					elif new_piece_input in ("Queen","queen","Q","q"):
						new_piece = "q"
						new_piece_input_works = True
					else:
						print("Please type a valid piece (Kings and Pawns are not allowed)")
		board64[old_moveend[-1]] = new_piece


def move_rook_is_legal(movestart,moveend):
	if abs(movestart-moveend) in (8,16,24,32,40,48,56) and (hit_detec(movestart,moveend) == True) and (board120[(move_convtr_64120(moveend))] in (can_take(movestart))):
		return True
	elif moveend in horiz_range(movestart) and (hit_detec(movestart, moveend) == True) and (board120[(move_convtr_64120(moveend))] in (can_take(movestart))):
		return True
	else:
		return False

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


def move_bishop_is_legal(movestart,moveend):
	if abs(movestart-moveend) in (7,14,21,28,35,42,49,9,18,27,36,45,54,63) and (hit_detec(movestart,moveend) == True) and (board120[(move_convtr_64120(moveend))] in (can_take(movestart))):
		return True
	else:
		return False

def move_queen_is_legal(movestart,moveend):
	if (move_bishop_is_legal(movestart,moveend) == True) or (move_rook_is_legal(movestart,moveend) == True):
		return True
	else:
		return False

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
	elif abs(movestart-moveend) == 2:
		move_king_sign2 = -abs(movestart-moveend) / (movestart-moveend)
		move_king_sign2 = int(move_king_sign2)
		if (board120[(move_convtr_64120(movestart))+(2*move_king_sign2)] == '0') and (hit_detec(movestart,moveend) == True):
			global old_movestart
			global old_moveend
			if ((iswhitemove == True) and (60 not in old_movestart)):
				if (((movestart-moveend) == 2) and (56 not in old_movestart) and (board120[move_convtr_64120(56)] == 'R')) or (((movestart-moveend) == -2) and (63 not in old_movestart) and (board120[move_convtr_64120(63)] == 'R')):
					return True
				else:
					return False
			elif ((iswhitemove == False) and (4 not in old_movestart)):
				if (((movestart-moveend) == 2) and (0 not in old_movestart) and (board120[move_convtr_64120(0)] == 'r')) or (((movestart-moveend) == -2) and (7 not in old_movestart) and (board120[move_convtr_64120(7)] == 'r')):
					return True
				else:
					return False
			else:
				return False
		else:
			return False
	else:
		return False

def castling_not_through_check(movestart,moveend):
	#global iswhitemove
	castling_movement_direc = (movestart-moveend) / abs(movestart-moveend)
	opp_eligible_moves()
	castling_inbetween_move = movestart-(1*castling_movement_direc)
	castling_inbetween_move = int(castling_inbetween_move)
	if castling_inbetween_move in (opp_eligible_move_end):
		return False
	else:
		return True

def castling():
	global old_movestart
	global old_moveend
	global castling_unmove_state
	castling_unmove_state = False
	if (len(old_moveend) > 0) and (board120[move_convtr_64120(old_moveend[-1])] in ('k','K')) and (abs((old_moveend[-1])-(old_movestart[-1])) == 2):
		castling_unmove_state = True
		if (old_movestart[-1] == 60) and (old_moveend[-1] == 62):
			force_move(63,61)
		elif (old_movestart[-1] == 60) and (old_moveend[-1] == 58):
			force_move(56,59)
		elif (old_movestart[-1] == 4) and (old_moveend[-1] == 6):
			force_move(7,5)
		elif (old_movestart[-1] == 4) and (old_moveend[-1] == 2):
			force_move(0,3)

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

def eligible_moves():
	global eligible_move_end
	global eligible_move_start
	eligible_move_end = []
	eligible_move_start = []
	possible_move_start = []
	test_possible_move_start = []
	possible_move_start = []
	test_possible_move_end = []
	if iswhitemove == True:
		for i in range(64):
			if board120[(move_convtr_64120(i))] in ('P','R','N','B','Q','K'):
				possible_move_start.append(i)
	else:
		for i in range(64):
			if board120[(move_convtr_64120(i))] in ('p','r','n','b','q','k'):
				possible_move_start.append(i)
	while len(possible_move_start) > 0:
		test_possible_move_start = possible_move_start.pop(0)
		if board120[move_convtr_64120(test_possible_move_start)] in ('p'):
			test_possible_move_end.extend((test_possible_move_start + 8, test_possible_move_start + 16, test_possible_move_start + 7, test_possible_move_start + 9))
		elif board120[move_convtr_64120(test_possible_move_start)] in ('P'):
			test_possible_move_end.extend((test_possible_move_start - 8, test_possible_move_start - 16, test_possible_move_start - 7, test_possible_move_start - 9))
		elif board120[move_convtr_64120(test_possible_move_start)] in ('R','r'):
			test_possible_move_end_rook_squares = [1,2,3,4,5,6,7,-1,-2,-3,-4,-5,-6,-7,8,16,24,32,40,48,56,-8,-16,-24,-32,-40,-48,-56]
			while len(test_possible_move_end_rook_squares) > 0:
				test_possible_move_end_rook = test_possible_move_end_rook_squares.pop(0)
				if (test_possible_move_start+test_possible_move_end_rook >= 0) and (test_possible_move_start + test_possible_move_end_rook <= 63):
					test_possible_move_end.append(test_possible_move_start + test_possible_move_end_rook)
		elif board120[move_convtr_64120(test_possible_move_start)] in ('N','n'):
			test_possible_move_end_knight_squares = [6,10,15,17,-6,-10,-15,-17]
			while len(test_possible_move_end_knight_squares) > 0:
				test_possible_move_end_knight = test_possible_move_end_knight_squares.pop(0)
				if (test_possible_move_start+test_possible_move_end_knight >= 0) and (test_possible_move_start + test_possible_move_end_knight <= 63):
					test_possible_move_end.append(test_possible_move_start + test_possible_move_end_knight)
		elif board120[move_convtr_64120(test_possible_move_start)] in ('B','b'):
			test_possible_move_end_bishop_squares = [7,14,21,28,35,42,49,9,18,27,36,45,54,63,-7,-14,-21,-28,-35,-42,-49,-9,-18,-27,-36,-45,-54,-63]
			while len(test_possible_move_end_bishop_squares) > 0:
				test_possible_move_end_bishop = test_possible_move_end_bishop_squares.pop(0)
				if (test_possible_move_start+test_possible_move_end_bishop >= 0) and (test_possible_move_start + test_possible_move_end_bishop <= 63):
					test_possible_move_end.append(test_possible_move_start + test_possible_move_end_bishop)
		elif board120[move_convtr_64120(test_possible_move_start)] in ('Q','q'):
			test_possible_move_end_queen_squares = [1,2,3,4,5,6,-1,-2,-3,-4,-5,-6,8,16,24,32,40,48,56,-8,-16,-24,-32,-40,-48,-56,7,14,21,28,35,42,49,9,18,27,36,45,54,63,-7,-14,-21,-28,-35,-42,-49,-9,-18,-27,-36,-45,-54,-63]
			while len(test_possible_move_end_queen_squares) > 0:
				test_possible_move_end_queen = test_possible_move_end_queen_squares.pop(0)
				if (test_possible_move_start+test_possible_move_end_queen >= 0) and (test_possible_move_start + test_possible_move_end_queen <= 63):
					test_possible_move_end.append(test_possible_move_start + test_possible_move_end_queen)
		elif board120[move_convtr_64120(test_possible_move_start)] in ('K','k'):
			test_possible_move_end_king_squares = [1,2,7,8,9,-1,-2,-7,-8,-9]
			while len(test_possible_move_end_king_squares) > 0:
				test_possible_move_end_king = test_possible_move_end_king_squares.pop(0)
				if (test_possible_move_start+test_possible_move_end_king >= 0) and (test_possible_move_start + test_possible_move_end_king <= 63):
					test_possible_move_end.append(test_possible_move_start + test_possible_move_end_king)
		while len(test_possible_move_end) > 0:
			possible_move_end = test_possible_move_end.pop(0)
			if (move_is_legal(test_possible_move_start,possible_move_end)) == True:
				eligible_move_start.append(test_possible_move_start)
				eligible_move_end.append(possible_move_end)

def both_eligible_moves():
	global iswhitemove
	iswhitemove = not iswhitemove
	eligible_moves()
	global opp_eligible_move_start
	global opp_eligible_move_end
	opp_eligible_move_start = eligible_move_start
	opp_eligible_move_end = eligible_move_end
	iswhitemove = not iswhitemove
	eligible_moves()

def opp_eligible_moves():
	global iswhitemove
	iswhitemove =  not iswhitemove
	eligible_moves()
	global opp_eligible_move_start
	global opp_eligible_move_end
	opp_eligible_move_start.clear()
	opp_eligible_move_end.clear()
	opp_eligible_move_start = eligible_move_start
	opp_eligible_move_end = eligible_move_end
	iswhitemove = not iswhitemove

def in_check():
	global iswhitemove
	global king_pos
	if iswhitemove == True:
		for i in range(64):
			if board120[move_convtr_64120(i)] == 'K':
				king_pos = i
	else:
		for i in range(64):
			if board120[move_convtr_64120(i)] == 'k':
				king_pos = i
	opp_eligible_moves()
	if king_pos in (opp_eligible_move_end):
		in_check = True
		return in_check
	else:
		in_check = False
		return in_check

def leads_to_check(movestart,moveend):
	if (test_move(movestart,moveend)) == True:
		upd_board_64120()
		global iswhitemove
		iswhitemove = not iswhitemove
		if (in_check()) == True:
			iswhitemove = not iswhitemove
			unmove()
			upd_board_64120()
			return True
		else:
			iswhitemove = not iswhitemove
			unmove()
			upd_board_64120()
			return False
	else:
		iswhitemove = not iswhitemove
		#print("Not an eligible move")

def in_check_moves():
	global in_check_eligible_move_start
	global in_check_eligible_move_end
	global iswhitemove
	in_check_eligible_move_start = []
	in_check_eligible_move_end = []
	both_eligible_moves()
	in_check_possible_eligible_move_start = eligible_move_start
	in_check_possible_eligible_move_end = eligible_move_end
	while len(in_check_possible_eligible_move_start) > 0:
		test_in_check_possible_eligible_move_start = in_check_possible_eligible_move_start.pop(0)
		test_in_check_possible_eligible_move_end = in_check_possible_eligible_move_end.pop(0)
		if (abs(test_in_check_possible_eligible_move_start-test_in_check_possible_eligible_move_end) == 2) and (board120[move_convtr_64120(test_in_check_possible_eligible_move_start)] in ('K','k')):
			if ((in_check()) == False) and (castling_not_through_check(test_in_check_possible_eligible_move_start,test_in_check_possible_eligible_move_end) == True):
				if (test_move(test_in_check_possible_eligible_move_start,test_in_check_possible_eligible_move_end)) == True:
					upd_board_64120()
					iswhitemove = not iswhitemove
					if (in_check()) == False:
						in_check_eligible_move_start.append(test_in_check_possible_eligible_move_start)
						in_check_eligible_move_end.append(test_in_check_possible_eligible_move_end)
					iswhitemove = not iswhitemove
					eligible_moves()
					unmove()
					upd_board_64120()
				else:
					iswhitemove = not iswhitemove
		elif (test_move(test_in_check_possible_eligible_move_start,test_in_check_possible_eligible_move_end)) == True:
			upd_board_64120()
			iswhitemove = not iswhitemove
			if (in_check()) == False:
				in_check_eligible_move_start.append(test_in_check_possible_eligible_move_start)
				in_check_eligible_move_end.append(test_in_check_possible_eligible_move_end)
			iswhitemove = not iswhitemove
			eligible_moves()
			unmove()
			upd_board_64120()
		else:
			iswhitemove = not iswhitemove

def end_conditions():
	in_check_moves()
	global old_movestart
	global old_moveend
	if len(in_check_eligible_move_start) == 0:
		if (in_check()) == True:
			if iswhitemove == True:
				print("Black Wins!")
				return False
			else:
				print("White Wins!")
				return False
		else:
			print("Draw by Stalemate")
			return False
	elif len(old_movestart) >= 8:
		if ((old_movestart[-8],old_moveend[-8]) == (old_moveend[-6],old_movestart[-6]) == (old_movestart[-4],old_moveend[-4]) == (old_moveend[-2],old_movestart[-2])) and ((old_movestart[-7],old_moveend[-7]) == (old_moveend[-5],old_movestart[-5]) == (old_movestart[-3],old_moveend[-3]) == (old_moveend[-1],old_movestart[-1])):
			print("Draw by Repetion")
			return False
		else:
			return True
	else:
		return True

def one_player():
	x = True
	global one_player
	global comp_goes_first
	global random_moves
	while x == True:
		player = input('Would you like to play in One player (versus the Computer) or Two player?\n')
		if player in ('one','One','1'):
			y = True
			while y == True:
				first_move = input('Would you like to go first or second?\n')
				if first_move in ('first','First','1st','1','one','One'):
					one_player = True
					comp_goes_first = False
					y = False
				elif first_move in ('second','Second','2nd','2','two','Two'):
					one_player = True
					comp_goes_first = True
					y = False
				elif first_move in ('exit','Exit','leave','Leave'):
					quit()
				else:
					print('Please type first or second to play. Otherwise type exit to leave.')
			while x == True:
				randomized_moves = input('Would you like the Computer to use random moves?\n')
				if randomized_moves in ('yes','Yes','yup','Yup','yeah','yeah'):
					random_moves = True
					x = False
				elif randomized_moves in ('no','No'):
					random_moves = False
					x = False
				elif randomized_moves in ('exit','Exit','leave','Leave'):
					quit()
				else:
					print('Please type yes or no to play. Otherwise type exit to leave.')
		elif player in ('two','Two','2'):
			one_player = False
			x = False
		elif player in ('exit','Exit','Leave','leave'):
			quit()
		else:
			print('Please type one or two to play. Otherwise type exit to leave.')

def board_eval():
	global white_board_eval
	global black_board_eval
	white_board_eval = 0
	black_board_eval = 0
	for i in range(64):
		if board64[i] == 'P':
			white_board_eval += 1
		elif board64[i] == 'p':
			black_board_eval += 1
		elif board64[i] == 'N':
			white_board_eval += 3
		elif board64[i] == 'n':
			black_board_eval += 3
		elif board64[i] == 'B':
			white_board_eval += 3
		elif board64[i] == 'b':
			black_board_eval += 3
		elif board64[i] == 'R':
			white_board_eval += 5
		elif board64[i] == 'r':
			black_board_eval += 5
		elif board64[i] == 'Q':
			white_board_eval += 9
		elif board64[i] == 'q':
			black_board_eval += 9
		elif board64[i] == 'K':
			white_board_eval += 500
		elif board64[i] == 'k':
			black_board_eval += 500

def play():
	while (end_conditions() == True):
		show_board()
		if iswhitemove == True:
			print("White's Move")
		else:
			print("Black's Move")
		#board_eval()
		#print("White Board Evaluation: ")
		#print(white_board_eval)
		#print("Black Board Evalutaion: ")
		#print(black_board_eval)
		#print(in_check_eligible_move_start)
		#print(in_check_eligible_move_end)
		if (one_player == False) or ((one_player == True) and iswhitemove != comp_goes_first):
			x = input('Starting move:\n')
			y = input('Ending move:\n')
			x = board_notation_convtr(x)
			y = board_notation_convtr(y)
		else:
			if random_moves == True:
				random_choice = len(in_check_eligible_move_start) - 1
				random_choice = random.randint(0,random_choice)
				x = in_check_eligible_move_start[random_choice]
				y = in_check_eligible_move_end[random_choice]
			else:
				print("Not Supported")
		move(x,y)
		upd_board_64120()
		castling()
		en_passant()
		pawn_promotion()
		upd_board_64120()

import random
upd_board_12064()
one_player()
play()
