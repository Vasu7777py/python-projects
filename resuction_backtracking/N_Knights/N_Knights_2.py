class Board:
	def __init__(self):
		self.Cells = []
		for _ in range(64):
			self.Cells.append(False)

	@ staticmethod
	def find_position(position:tuple):
		return ((position[0] * 8) + position[1])

	@staticmethod
	def is_inside_border(position:tuple):
		x, y = position
		if ((x >= 0) and (x < 8) and (y >= 0) and (y < 8)):
			return True
		else:
			return False

class N_Knights(Board):
	def __init__(self):
		Board.__init__(self)
		self.Moves = []

	def is_completed(self):
		count = 0
		for checked in self.Cells:
			if checked:
				count += 1
		if (count == 64):
			return True
		else:
			return False

	def posible_moves(self, position:tuple):
		x, y = position
		#       up_left,        up_right,     right_up,      right_down,  down_right,  down_left,     left_up,      left_down
		check = [(x -1, y -2), (x +1, y -2), (x +2, y -1), (x +2, y +1), (x +1, y +2), (x -1, y +2), (x -2, y -1), (x -2, y +1)]
		moves = []
		for move in check:
			if Board.is_inside_border(move):
				if (not self.Cells[Board.find_position(move)]):
					moves.append(move)
		return moves

	def run(self, move:tuple):
		self.Moves.append((move, Board.find_position(move)) )
		self.Cells[Board.find_position(move)] = True
		if self.is_completed():
			return True
		else:
			for Move in self.posible_moves(move):
				if self.run(Move):
					return True
				self.Moves.remove((Move, Board.find_position(Move)) )

		return False

def main():
	N = N_Knights()
	N.run((0, 0))
	print(N.Moves)

if __name__ ==  "__main__":
	main()
