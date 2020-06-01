
class Board:
	def __init__(self):
		self.cells = []
		for x in range(8):
			for y in range(8):
				self.cells.append(Cell((x, y)))

	@staticmethod
	def find_cell_pos(position:tuple):
		return ((position[0] * 8) + position[1])

class Cell:
	def __init__(self, position:tuple):
		self.position = position
		self.checked = False

def main():
	b = Board()
	print(b.cells[Board.find_cell_pos((6, 7))].position)

if __name__ == '__main__':
	main()

