import tkinter as tk
import ChessPices
import TrackerMovement as TM

starting = True
Board = [[],[],[],[],[],[],[],[]]

class Theme:
    def __init__(self):
        self.themes = {
                "Default" : {
                    "cell_Dark" : "#000000",#black
                    "cell_text_on_Dark" : "#FFFFFF",#White
                    "cell_bright" : "#FFFFFF",#White
                    "cell_text_on_Bright" : "#000000",#black
                    "Selected" : "#CC00CC",#mengenta
                    "move_to" : "#33FF33" #lime Green
                },
                "Stone_age": {
                    "cell_Dark": "#404040",#grey
                    "cell_text_on_Dark": "#FFFFFF",#White
                    "cell_bright" : "#E0E0E0",#light grey
                    "cell_text_on_Bright" : "#000000",#black
                    "Selected" : "#009999",#cyan
                    "move_to" : "#CC0000",#red
                }
            }
        
        self.themes_list = []
        for theme in self.themes:
            self.themes_list.append(theme)

        self.number_of_themes = len(self.themes_list)

        self.selected_theme_name = self.themes_list[0]
        self.selected_theme = self.themes[self.selected_theme_name]

    def next_theme(self):
        theme_index = self.themes_list.index(self.selected_theme_name)

        if ( (theme_index + 1) <= (self.number_of_themes - 1) ):
            self.selected_theme_name = self.themes_list[theme_index + 1]
        else:
            self.selected_theme_name = self.themes_list[0]

        self.selected_theme = self.themes[self.selected_theme_name]
        theme_reset()

    def previous_theme(self):
        theme_index = self.themes_list.index(self.selected_theme_name)
        if ( (theme_index - 1) >= 0 ):
            self.selected_theme_name = self.themes_list[theme_index - 1]
        else:
            self.selected_theme_name = self.themes_list[self.number_of_themes - 1]

        self.selected_theme = self.themes[self.selected_theme_name]
        theme_reset()

theme = Theme()

# Creating a main frame where all the wigeds are 
# being added
# here "700x600" is the width * height

root = tk.Tk()
root.geometry("700x600")
root.title("CHESS")

Board_Lable = tk.LabelFrame(height=32, width=56)
Terminal = tk.LabelFrame(height=32, width=30)
Task = tk.LabelFrame(height=7, width=86)

Task.grid(row=0, column=0)
Terminal.grid(row=1, column=0)
Board_Lable.grid(row=1, column=1)

next_theme = tk.Button(Terminal, height=3, width=7, command = theme.next_theme, text = "next\ntheme")
previous_theme = tk.Button(Terminal, height=3, width=7, command = theme.previous_theme, text = "previous\ntheme")
next_theme.pack()
previous_theme.pack()

# creating empty slots in a list to add Buttons later

def get_tag(position:tuple):
    x, y = position[0], position[1]
    Tcell = TM.Tracker[x][y]
    if Tcell["Value"] != None:
        value = Tcell["object"]
        text_tag = value.get_pice_id() + "\n" +  value.get_ColourOfPice()
    else:text_tag = ""
    return text_tag

class Cell:
    def __init__(self, position:tuple, back_ground_colour:str, text_colour:str):
        self.position = position
        self.back_ground_colour = back_ground_colour
        self.text_colour = text_colour
        self.Button = tk.Button(Board_Lable, height=4, width=7, bg = self.back_ground_colour, fg = self.text_colour)

    def Button_update(self, selected_position:tuple, Scolour:str, Mcolour:str, positions:list):
        value = TM.Tracker[selected_position[0]][selected_position[1]]
        if value["Value"] != None:
            value["State"] = TM.active
            x, y = selected_position[0], selected_position[1]
            text_tag = get_tag((x, y))
            self.back_ground_colour = Scolour
            self.Button = tk.Button(Board_Lable, height = 4, width = 7, fg = self.text_colour, bg = self.back_ground_colour, text= text_tag, command = self.reset)

            for moves in positions:
                x, y = moves[0], moves[1]
                value = TM.Tracker[x][y]
                value["State"] = TM.active
                text_tag = get_tag((x, y))
                cell = Board[x][y]
                cell.back_ground_colour = Mcolour
                cell.Button = tk.Button(Board_Lable, height = 4, width = 7, fg = cell.text_colour, bg = cell.back_ground_colour, text= text_tag, command = cell.Move_Pice)
        else:
            TM.Waiting_For_Pice_Movement = False
          
    def clicked(self):
        value = TM.Tracker[self.position[0]][self.position[1]]
        if (not(TM.Waiting_For_Pice_Movement) and (value["State"] != TM.active) ):
            TM.Waiting_For_Pice_Movement = True
            TM.selected = self.position
            positions = TM.find_posible_moves(self.position)
            self.Button_update(self.position, theme.selected_theme["Selected"], theme.selected_theme["move_to"], positions)
        else:
            self.Button_reset()
        PrintBoard()
    
    def Button_reset(self):
        TM.Waiting_For_Pice_Movement = False
        TM.selected = None
        for x in range(8):
            for y in range(8):
                value = TM.Tracker[x][y]
                if (value["State"] == TM.active):
                    value["State"] = not(TM.active)
                    cell = Board[x][y]
                    if( ( ((x % 2) == 0) and ((y % 2) != 0) ) or ( ((x % 2) != 0) and ((y % 2) == 0) ) ):
                        cell.back_ground_colour = theme.selected_theme["cell_Dark"]
                    else:
                        cell.back_ground_colour = theme.selected_theme["cell_bright"]
                    text_tag = get_tag((x, y))
                    cell.Button = tk.Button(Board_Lable, height = 4, width = 7, fg = cell.text_colour, bg = cell.back_ground_colour, text= text_tag, command = cell.clicked)

    def reset(self):
        self.Button_reset()
        PrintBoard()

    def Move_Pice(self):
        Selected_Pice_Position = TM.selected
        To_Position = self.position
        pice = TM.Tracker[Selected_Pice_Position[0]][Selected_Pice_Position[1]]["object"].get_pice_id()
        TM.Move_Pice(Selected_Pice_Position, To_Position, pice)
        self.reset()

# to generate a empty chess board with 2d array of buttons
def GenerateBoard():
    for x in range(8):
        for y in range(8):
            position = (x, y)
            if( ( ((x % 2) == 0) and ((y % 2) != 0) ) or ( ((x % 2) != 0) and ((y % 2) == 0) ) ):
                Board[x].append(Cell(position, theme.selected_theme["cell_Dark"], theme.selected_theme["cell_text_on_Dark"]))
            else:
                Board[x].append(Cell(position, theme.selected_theme["cell_bright"], theme.selected_theme["cell_text_on_Bright"]))

# to place pices in board as per as rules of chess
Default_Board_Placement = ChessPices.Default_Pice_setup()
def start_Board(Default_Board_Placement):
    
    TM.start_set_up(Default_Board_Placement)

    for x in range(8):
        for y in range(8):
            text_tag = get_tag((x, y))
            cell = Board[x][y]
            cell.Button = tk.Button(Board_Lable, height = 4, width = 7, fg = cell.text_colour, bg = cell.back_ground_colour, text= text_tag, command = cell.clicked)

def theme_reset():
    for x in range(8):
        for y in range(8):
            cell = Board[x][y]
            if( ( ((x % 2) == 0) and ((y % 2) != 0) ) or ( ((x % 2) != 0) and ((y % 2) == 0) ) ):
                cell.back_ground_colour = theme.selected_theme["cell_Dark"]
                cell.text_colour = theme.selected_theme["cell_text_on_Dark"]
            else:
                cell.back_ground_colour = theme.selected_theme["cell_bright"]
                cell.text_colour = theme.selected_theme["cell_text_on_Bright"]

            text_tag = get_tag((x, y))
            cell.Button = tk.Button(Board_Lable, height = 4, width = 7, fg = cell.text_colour, bg = cell.back_ground_colour, text= text_tag, command = cell.clicked)
    Board[0][0].reset()

def PrintBoard():
    for x in range(8):
        for y in range(8):
            cell = Board[x][y]
            cell.Button.grid(row=y, column=x)

def main(starting):
    if starting:
        GenerateBoard()
        start_Board(Default_Board_Placement)
        starting = False
        
    PrintBoard()

if __name__ == "__main__":
    main(starting)

root.mainloop()