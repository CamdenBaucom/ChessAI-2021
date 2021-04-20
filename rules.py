board120 = ['-1','-1','-1','-1','-1','-1','-1','-1','-1','-1',
'-1','-1','-1','-1','-1','-1','-1','-1','-1','-1',
'-1','0','1','2','3','4','5','6','7','-1',
'-1','8','9','10','11','12','13','14','15','-1',
'-1','16','17','18','19','20','21','22','23','-1',
'-1','24','25','26','27','28','29','30','31','-1',
'-1','32','33','34','35','36','37','38','39','-1',
'-1','40','41','42','43','44','45','46','47','-1',
'-1','48','49','50','51','52','53','54','55','-1',
'-1','56','57','58','59','60','61','62','63','-1',
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
boardstrnew = ""
boardstr = ""

def show_board():
#	boardstr = ""
#	for i in range(64):
#		boardstrold = "][".join(board64[i])
#		global boardstrnew 
#		boardstr = boardstrnew + boardstrold
	for z in range(1,9):
		y = (z-1)*8
		x = z*8
		for i in range(y,x):
			board64short.append(board64[i])
			# return board64short
			boardstrstart = "["
			boardstrend = "]"
			boardstrmid = ']['.join(map(str, board64short))
		boardstrnew = boardstrstart+boardstrmid+boardstrend+"\n"
		#return boardstrnew
		global boardstr
		boardstrold = boardstrnew
		boardstr = boardstrold+boardstrnew
		#boardstrnew = boardstrstart+boardstrmid+boardstrend+"\n"
		# return boardstrnew
	# return board64short
	return boardstr
	# return x
	# return i
print(show_board())

# print(' '.join(map(str, board64)))
# print(board64[1])

