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
	elif board120[(move_convtr_64120(movestart))] == 'K' or 'K':
		move_king_is_legal(movestart,moveend)
	else:
		return False

def move_pawn_is_legal(movestart,moveend):
	if movestart == moveend + 8 or moveend - 8:
		if board120[(move_convtr_64120(moveend))] == '0':
			return True
		else:
			return False
	else:
		return False

def move_rook_is_legal(movestart,moveend):
	if (movestart-moveend) in (8,16,24,32,40,48,56,-8,-16,-24,-32,-40,-48,-56):
		return True


upd_board_12064()
# print(move_rook_is_legal(52,44))
# show_board()
