import numpy as np

Board_rows = 6
Board_col = 7
winnig_coin_count = 4
Board = np.zeros((Board_rows ,Board_col) ,int)

Player_Red = 1
Player_Blue = 2

# To print the board
board_list = [1, 2, 3, 4, 5, 6]
def Print_Board(Board):
    print(board_list)
    print(np.flip(Board ,0))

# To check if the selected column is valid to add the coin
def Is_Avaliable(Board ,col):
    if Board[Board_rows - 1][col] == 0:
        return True
    else:
        return False

# To search in which row to add the coin
def Search_row(Board ,col):
    for row in range(Board_rows):
        if Board[row][col] == 0:
            return(row)

# To add the coin
def Add_pice(Board ,row ,col ,Player):
    Board[row][col] = Player

# winning logic

# checks if the game is draw or not and returns a bool
def Draw_condition(Player_Red_chance ,Player_Blue_chance):
    return ((Player_Red_chance + Player_Blue_chance) == 0)

# this function counts the coins of the selected player ,
# from last added coin position and in a set direction passed by Is_Game_over() function;
# and returns how many coins are there in the set direction 
def Count_coins(Board ,Player ,Last_row ,last_col ,direction):
    count_coin = 0

    cur_row = Last_row
    cur_col = last_col
    cur_coin = Board[Last_row][last_col]
    while cur_coin == Player: 
        count_coin += 1
        cur_row += direction[0]
        cur_col += direction[1]

        if (cur_row >= 0) and (cur_row < Board_rows) and (cur_col >= 0) and (cur_col < Board_col):
            cur_coin = Board[cur_row][cur_col]
        else:
            cur_coin = 0

    # this count_coin includes the coin which is last added and shearched
    # so the least value returned is 1 <which is the last added coin its self>
    return count_coin

# checks all the direction by the help of Count_coins() function,
# from last added positon; and sees if the last played player has won or not;
# this function runs all the time the player makes a valid move
def Is_Game_over(Board ,last_row ,last_col ,Player):
    direction = {
        "up" : [1 ,0],
        "up_right" : [1 ,1],
        "right" : [0 ,1],
        "down_right" : [-1 ,1],
        "down" : [-1 ,0],
        "down_left" : [-1 ,-1],
        "left" : [0 ,-1],
        "up_left" : [1 ,-1]
    }

    # this dict stores how many coins is there arround the last added coin
    direction_count = {}

    for direct in direction:
        direction_count[direct] = Count_coins(Board ,Player ,last_row ,last_col ,direction[direct])
    
    for direct_count in direction_count:
        if direction_count[direct_count] == winnig_coin_count:
            return True
    
    # here (direction_count[dircetion] + direction_count[complement dircetion] - 1),
    # the <- 1> is because the value returned from Count_coins() function inclueds the coin which is last added and shearched,
    # so both direction_count[dircetion] and direction_count[complement dircetion] contanes the last added coin counted,
    # we can over come that by subracting that extra counted coin
    if (direction_count["up"] + direction_count["down"] -1 ) >= winnig_coin_count:
        return True
    elif (direction_count["up_right"] + direction_count["down_left"] -1 ) >= winnig_coin_count:
        return True
    elif (direction_count["right"] + direction_count["left"] -1 ) >= winnig_coin_count:
        return True
    elif (direction_count["down_right"] + direction_count["up_left"] -1 ) >= winnig_coin_count:
        return True
    else:
        return False

# MAIN function of the program
def main(Board ,Player_Red ,Player_Blue):
    Print_Board(Board)
    is_game_over = False
    
    Player_Red_chance = 21
    Player_Blue_chance = 21
    Player = 1
    while not is_game_over:
        if Player == 1:
            col = (int(input("RED PLAYER : Select the column : ")) - 1 )
            if col <= Board_rows: # Checking if entered column is valid
                check = Is_Avaliable(Board ,col)
                if check:
                    row = Search_row(Board ,col)
                    Add_pice(Board ,row ,col ,Player_Red)
                    Player_Red_chance -= 1
                    Print_Board(Board)
                    Is_draw = Draw_condition(Player_Red_chance ,Player_Blue_chance)
                    if Is_draw:
                        print("THE HAS GONE TO DRAW TRY AGAIN")
                        is_game_over = True
                    else:
                        is_game_over = Is_Game_over(Board ,row ,col ,Player_Red)
                        if is_game_over:
                            print("RED PLAYER has won the game....")
                    Player = 2 # changing from player 1 to 2
                else:
                    print("COLUMN IS FULL TRY ANY OTHER COLUMN : ")
            else:
                print("IVALID COLUMN TRY ANY OTHER COLUMN : ")
        else:
            col = (int(input("BLUE PLAYER : Select the column : ")) - 1 )
            if col <= Board_rows: # Checking if entered column is valid
                check = Is_Avaliable(Board ,col)
                if check:
                    row = Search_row(Board ,col)
                    Add_pice(Board ,row ,col ,Player_Blue)
                    Player_Blue_chance -= 1
                    Print_Board(Board)
                    Is_draw = Draw_condition(Player_Red_chance ,Player_Blue_chance)
                    if Is_draw:
                        print("THE HAS GONE TO DRAW TRY AGAIN")
                        is_game_over = True
                    else:
                        is_game_over = Is_Game_over(Board ,row ,col ,Player_Blue)
                        if is_game_over:
                            print("BLUE PLAYER has won the game....")
                    Player = 1 # changing from player 2 to 1
                else:
                    print("COLUMN IS FULL TRY ANY OTHER COLUMN : ")
            else:
                print("IVALID COLUMN TRY ANY OTHER COLUMN : ")

if __name__ == "__main__":
    main(Board ,Player_Red ,Player_Blue)
