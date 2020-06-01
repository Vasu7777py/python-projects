import tkinter as tk

starting = True

root = tk.Tk()
root.geometry("700x600")
root.title("CHESS")

class Cell:
    def __init__(self, position:tuple, Bcolour:str, Tcolour:str, text:str):
        self.position = position
        self.Bcolour = Bcolour
        self.Tcolour = Tcolour
        self.Button = tk.Button(root, height=4, width=7, bg = self.Bcolour, fg = self.Tcolour, text = text, command = self.clicked)
    
    def clicked(self):
        print(self.position)

Board = [[],[],[],[],[],[],[],[]]

def GenerateBoard():
    for x in range(8):
        for y in range(8):
            position = (x, y)
            if( ( ((x % 2) == 0) and ((y % 2) != 0) ) or ( ((x % 2) != 0) and ((y % 2) == 0) ) ):
                Board[x].append(Cell(position, "Black", "white", "hii"))
            else:
                Board[x].append(Cell(position, "white", "Black", "hii"))
                
def PrintBoard():
    for x in range(8):
        for y in range(8):
            cell = Board[x][y]
            cell.Button.grid(row=y, column=x)

def main(starting):
    if starting:
        GenerateBoard()
        starting = False
        
    PrintBoard()

if __name__ == "__main__":
    main(starting)

root.mainloop()