from Board import Board

board = Board()
Moves = []

def is_completd():
	count = 0
	for cell in board.cells:
		if cell.checked:
			count += 1
	if count == 64:
		return True
	else:
		return False

def check_border_condition(moves:list):
	print(moves)
	for move in moves:
		print(move)
		x, y = move
		if not ((x >= 0) and (x < 8) and (y >= 0) and (y < 8)):
			moves.remove(move)
	return moves

def Knight_moves(position:tuple):
	x, y = position
	check = [(x -1, y -2), (x +1, y -2), (x +2, y -1), (x +2, y +1), (x +1, y +2), (x -1, y +2), (x -2, y -1), (x -2, y +1)]
	moves = check_border_condition(check)
	for move in moves:
		if (board.cells[Board.find_cell_pos(move)].checked):
			moves.remove(move)
	return moves

def run(position:tuple):
	board.cells[Board.find_cell_pos(position)].checked = True
	Moves.append(position)
	if is_completd():
		return True
	else:
		for move in Knight_moves(position):
			if run(move):
				return True
			Moves.remove(move)

	return False

def main():
	run((0, 0))
	print(*Moves)

if __name__ ==  "__main__":
	main()
