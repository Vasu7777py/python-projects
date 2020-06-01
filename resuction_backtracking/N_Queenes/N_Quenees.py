
class Cell:
	def __init__(self):
		self.Contains_Queen = False
		self.Is_under_control = False

class Board:
	def __init__(self):
		self.Cells = []
		for _ in range(64):
			self.Cells.append(Cell())

	"""
	56	57	58	59	60	61	62	63
	48	49	50	51	52	53	54	55
	40	41	42	43	44	45	46	47
	32	33	34	35	36	37	38	39
	24	25	26	27	28	29	30	31
	16	17	18	19	20	21	22	23
	8	9	10	11	12	13	14	15
	0	1	2	3	4	5	6	7
	"""

	@staticmethod
	def find_cell(position:tuple):
		return ((position[1] * 8) + position[0])

	@staticmethod
	def Is_inside_border(position:tuple):
		x, y = position
		if ((x >= 0) and (x < 8) and (y >= 0) and (y < 8)):
			return True
		else:
			return False

class N_Queens(Board):
	def __init__(self):
		Board.__init__(self)
		self.queens_placed = []

	def is_completed(self):
		count = 0
		for cell in self.Cells:
			if (cell.Contains_Queen or cell.Is_under_control):
				count += 1
		if ((count == 64) ):#and (len(self.queens_placed) == 8)
			return True
		else:
			return False

	def occupy_cells(self, Move:tuple):
		x, y = Move
		direction = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, +1)]
		for direct in direction:
			tempx, tempy = x, y
			deadend = False
			x_direct, y_direct = direct
			while not deadend:
				tempx += x_direct
				tempy += y_direct
				if Board.Is_inside_border((tempx, tempy)):
					self.Cells[Board.find_cell((tempx, tempy))].Is_under_control = True
				else:
					deadend = True

	def unouccpy_cells(self, Move:tuple):
		x, y = Move
		direction = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, +1)]
		for direct in direction:
			tempx, tempy = x, y
			deadend = False
			x_direct, y_direct = direct
			while not deadend:
				tempx += x_direct
				tempy += y_direct
				if Board.Is_inside_border((tempx, tempy)):
					self.Cells[Board.find_cell((tempx, tempy))].Is_under_control = False
				else:
					deadend = True

		for queen in self.queens_placed:
			N_Queens.occupy_cells(queen)

	def nxt_queen(self, position:tuple):
		posible_positions = []
		for cell_index in range(64):
			if not (self.Cells[cell_index].Is_under_control and self.Cells[cell_index].Contains_Queen):
				posible_positions.append((cell_index - (cell_index//8), cell_index//8))
		return posible_positions

	def run(self, Move:tuple = (0, 0)):
		self.queens_placed.append(Move)
		self.Cells[Board.find_cell(Move)].Contains_Queen = True
		self.occupy_cells(Move)
		if self.is_completed():
			return True
		else:
			for move in self.nxt_queen(Move):
				if self.run(Move):
					return True
				self.queens_placed.remove(move)
				self.unouccpy_cells(move)

		return False

def main():
	queen = N_Queens()
	print(queen.run())
	print(queen.queens_placed)

if __name__ == "__main__":
	main()
