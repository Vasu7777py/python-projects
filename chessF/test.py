import tkinter as tk
from dataclasses import dataclass

root = tk.Tk()
root.geometry("700x600")
root.title("CHESS")

Cells = [[],[],[],[],[],[],[],[]]

for x in range(8):
    for y in range(8):
        if( ( ((x % 2) == 0) and ((y % 2) != 0) ) or ( ((x % 2) != 0) and ((y % 2) == 0) ) ):
            Cells[x].append(tk.Button(root ,bg = "black",height=4,width=7))
        else:
            Cells[x].append(tk.Button(root ,height=4,width=7))

pic = tk.PhotoImage("bqueen.png",height=4,width=7)
Cells[6][4] = tk.Button(root ,image=pic ,height=4,width=7)

for x in range(8):
    for y in range(8):
        Cells[x][y].grid(row=y, column=x)

root.mainloop()