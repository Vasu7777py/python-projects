import tkinter as tk
import numpy as np

Board_rows = 6
Board_col = 7
winnig_coin_count = 4
Board = np.zeros((Board_rows ,Board_col) ,int)

Player_Red = 1
Player_Blue = 2

main = tk.Tk()

for x in range(Board_rows):
    for y in range(Board_col):
        coin = tk.Label(main ,text = Board[x][y])
        coin.grid(column = y ,row = x)
main.mainloop()