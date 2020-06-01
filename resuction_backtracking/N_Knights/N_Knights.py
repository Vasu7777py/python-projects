from Board import Board

class N_Knights(Board):
	def __init__(self):
		Board.__init__(self)
		self.moves = []

	def is_completed(self):
		count = 0
		for cell in range(64):
			if self.cells[cell].checked:
				count += 1
		if count == 64:
			return True
		else:
			return False

	def run(self, position:tuple):
		print(f"\"{position}\"")
		self.cells[Board.find_cell_pos(position)].checked = True
		self.moves.append(position)
		print(f"\"\"{self.moves}\"\"")
		if self.is_completed():
			return True
		else:
			for move in self.Knight_moves(position):
				if self.run(tuple(move)):
					return True
				self.moves.remove(tuple(move))

		return False

	def check_border_condition(self, Moves:list):
		print(Moves, range(len(Moves)))
		for index in range(len(Moves)):
			x, y = Moves[index][0], Moves[index][1]
			print(index ,Moves[index])
			if not ((x >= 0) and (x < 8) and (y >= 0) and (y < 8)):
				Moves.remove(Moves[index])
		print(Moves)
		return Moves

	def Knight_moves(self, position:tuple):
		x, y = position
		moves = [[x -1, y -2], [x +1, y -2], [x +2, y -1], [x +2, y +1], [x +1, y +2], [x -1, y +2], [x -2, y -1], [x -2, y +1]]
		moves = self.check_border_condition(moves)
		for move in moves:
			if (self.cells[Board.find_cell_pos(tuple(move))].checked):
		 		moves.remove(move)
		return moves

def main():
	n = N_Knights()
	n.run((0,0))
	print(*n.moves)

if __name__ ==  "__main__":
	main()
