board120 = ['-1','-1','-1','-1','-1','-1','-1','-1','-1','-1',
'-1','-1','-1','-1','-1','-1','-1','-1','-1','-1',
'-1','r','n','b','q','k','b','n','r','-1',
'-1','p','p','p','p','p','p','p','p','-1',
'-1','0','0','0','0','0','0','0','0','-1',
'-1','0','0','0','0','0','0','0','0','-1',
'-1','0','0','0','0','0','0','0','0','-1',
'-1','p','0','0','0','0','0','0','0','-1',
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

board64short = []
boardstr = ""

def show_board():
	for z in range(1,9):
		y = (z-1)*8
		x = z*8
		for i in range(y,x):
			board64short.append(board64[i])
			boardstrstart = "["
			boardstrend = "]"
			boardstrmid = ']['.join(map(str, board64short))
		boardstrnew = ""
		boardstrnew = boardstrstart+boardstrmid+boardstrend+"\n"
		global boardstr
		boardstr = boardstr+boardstrnew
		board64short.clear()
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

move_convtr_64120_var1 = 0
move_convtr_64120_var2 = 0

def move_convtr_64120(movestart):
	for a in range(movestart):
		if a in (8,9,18,19,28,29,38,39,48,49,58,59):
			global move_convtr_64120_var1
			move_convtr_64120_var1 += 1
	for b in range(movestart + move_convtr_64120_var1):
		if b in (8,9,18,19,28,29,38,39,48,49,58,59,68,69):
			global move_convtr_64120_var2
			move_convtr_64120_var2 +=1
	if (movestart + move_convtr_64120_var1) in (8,9,18,19,28,29,38,39,48,49,58,59,68,69):
		move_convtr_64120_var2 += 2
	movestart = movestart + move_convtr_64120_var2 + 21
	move_convtr_64120_var1 = 0
	move_convtr_64120_var2 = 0
	return movestart

last_movestart = 0
last_moveend = 0

def move(movestart,moveend):
	movestart -= 1
	moveend -= 1
	if move_pawn_is_legal(movestart,moveend):
		board64[moveend] = board64[movestart]
		board64[movestart] = 0
		print("Possible")
		global last_movestart
		last_movestart = movestart
		global last_moveend
		last_moveend = moveend
	else:
		print("Not possible")

def move_is_legal(movestart,moveend):
	if board120[(move_convtr_64120(movestart))] == 'p' or 'P':
		move_pawn_is_legal(movestart,moveend)
	elif board120[(move_convtr_64120(movestart))] == 'r' or 'R':
		move_rook_is_legal(movestart,moveend)
	elif board120[(move_convtr_64120(movestart))] == 'n' or 'N':
		move_knight_is_legal(movestart,moveend)
	elif board120[(move_convtr_64120(movestart))] == 'b' or 'B':
		move_bishop_is_legal(movestart,moveend)
	elif board120[(move_convtr_64120(movestart))] == 'q' or 'Q':
		move_queen_is_legal(movestart,moveend)
	elif board120[(move_convtr_64120(movestart))] == 'k' or 'K':
		move_king_is_legal(movestart,moveend)
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
	elif (movestart == moveend + (16*pawn_move_direction)) and ((board120[(move_convtr_64120(movestart))] == 'p' and movestart in (8,9,10,11,12,13,14,15)) or (board120[(move_convtr_64120(movestart))] == 'P' and movestart in (48,49,50,51,52,53,54,55))):
		if (hit_detec(movestart,moveend) == True):
			return True
		else:
			return False
	elif (movestart == (moveend + 7*pawn_move_direction) or (moveend + 9*pawn_move_direction)) and board120[(move_convtr_64120(moveend))] != 0 or -1:
		if movestart not in (8,16,24,32,40,48,15,23,31,39,47,55):
			return True
		elif movestart == moveend + 7*pawn_move_direction and ((pawn_move_direction == -1 and movestart in (15,23,31,39,47,55)) or (pawn_move_direction == 1 and movestart in (8,16,24,32,40,48))):
			return True
		elif movestart == moveend + 9*pawn_move_direction and ((pawn_move_direction == -1 and movestart in (8,16,24,32,40,48)) or (pawn_move_direction == 1 and movestart in (15,23,31,39,47,55))):
			return True
		else:
			return False
	else:
		return False


def move_rook_is_legal(movestart,moveend):
	if (movestart-moveend) in (8,16,24,32,40,48,56,-8,-16,-24,-32,-40,-48,-56):
		return True

def hit_detec(movestart,moveend):
	movestart -= 1
	moveend -= 1
	hit_detec_sign = (moveend-movestart) / abs(moveend-movestart)
	hit_detec_sign = int(hit_detec_sign)
	if abs(movestart-moveend) in (8,16,24,32,40,48,56,64):
		hit_detec_horiz_counter = abs(((movestart-moveend) / 8)) + 1
		hit_detec_horiz_counter = int(hit_detec_horiz_counter)
		hit_detec_horiz_bool = False
		for i in range(hit_detec_horiz_counter):
			hit_detec_horiz_between = i*8
			if hit_detec_horiz_between == 0:
				hit_detec_horiz_bool = False
			elif board120[(move_convtr_64120(movestart+(hit_detec_sign*hit_detec_horiz_between)))] == '0':
				hit_detec_horiz_bool = True
			else:
				hit_detec_horiz_bool = False
				return hit_detec_horiz_bool
		return hit_detec_horiz_bool
	elif (abs(movestart-moveend) in (1,2,3,4,5,6)) or (abs(movestart-moveend) == 7 and (movestart and moveend) in (0,8,16,24,32,40,48,56,7,15,23,31,39,47,55,63)):
		hit_detec_vert_counter = abs(movestart-moveend) + 1
		hit_detec_vert_counter = int(hit_detec_vert_counter)
		hit_detec_vert_bool = False
		for i in range(hit_detec_vert_counter):
			print(i)
			if i == 0:
				hit_detec_vert_bool = False
			elif board120[(move_convtr_64120(movestart+(hit_detec_sign*i)))] == '0':
				hit_detec_vert_bool = True
			else:
				hit_detec_vert_bool = False
				return hit_detec_vert_bool
		return hit_detec_vert_bool
	else:
		if abs(movestart-moveend) in (7,14,21,28,35,42,49):
			hit_detec_diag_counter = abs(((movestart-moveend) / 7)) + 1
			hit_detec_diag_inc = 7
		else:
			hit_detec_diag_counter = abs(((movestart-moveend) / 9)) + 1
			hit_detec_diag_inc = 9
		hit_detec_diag_counter = int(hit_detec_diag_counter)
		hit_detec_diag_bool = False
		for i in range(hit_detec_diag_counter):
			hit_detec_diag_between = i*hit_detec_diag_inc
			if hit_detec_diag_between == 0:
				hit_detec_diag_bool = False
			elif board120[(move_convtr_64120(movestart+(hit_detec_sign*hit_detec_diag_between)))] == '0':
				hit_detec_diag_bool = True
			else:
				hit_detec_diag_bool = False
				return hit_detec_diag_bool
		return hit_detec_diag_bool

upd_board_12064()
print(move_pawn_is_legal(40,47))
# print(move_rook_is_legal(52,44))
# show_board()
