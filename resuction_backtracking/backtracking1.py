import time

board = [
    [0,2,0,0,0,0,0,0,0],
    [0,0,0,6,0,0,0,0,3],
    [0,7,4,0,8,0,0,0,0],
    [0,0,0,0,0,3,0,0,2],
    [0,8,0,0,4,0,0,1,0],
    [6,0,0,5,0,0,0,0,0],
    [0,0,0,0,1,0,7,8,0],
    [5,0,0,0,0,9,0,0,0],
    [0,0,0,0,0,0,0,4,0]
]

def print_board(board_:list):
    for row in range(len(board_)):
        if ( (row % 3 == 0) and (row != 0) ):
            print("- - - - - - - - - - -")
        
        for col in range(len(board_[0])):
            if ( (col % 3 == 0) and (col != 0) ):
                print("| ", end="")

            if (col == 8):
                print(board_[row][col])
            else:
                print(f"{board_[row][col]} ", end = "")

def find_nxt_empty(board_:list):
    for row in range(len(board_)):
        for col in range(len(board_[0])):
            if (board_[row][col] == 0):
                return (row, col)
    
    return True

def is_valid(board_, num, position):
    row_p, col_p = position
    print(f" position {position} ", end = "")
    # checking row
    row = board_[row_p]
    col_num = 0
    for col in row:
        if ( (col == num) and (col_num != col_p) ):
            print(f" row {row_p} {col_num} ", end = "")
            return False
        col_num += 1


    #checking col
    col = []
    for row in board_:
        col.append(row[col_p])
    row_num = 0
    for row in col:
        if ( (row == num) and ( row_num != row_p) ):
            print(f" col {row_num} {col_p} ", end = "")
            return False
        row_num += 1
    
    # checking box

    box_x = col_p // 3
    box_y = row_p // 3

    for col_loop in range(box_x*3, box_x*3 + 3):
        for row_loop in range(box_y*3, box_y*3 +3):
            if ( (board_[row_loop][col_loop] == num) and ((row_loop, col_loop) != position) ):
                print(f" box_x {box_x} box_y {box_y} row {row_loop} col {col_loop} ", end = "")
                return False
    
    return True


def solve_board(board_):
    print_board(board_)
    position = find_nxt_empty(board_)
    print("\n\n")
    if not position:
        return True
    else:
        row, col = position
    
    for num in range(1,10):
        print(f" num {num} ", end = "")
        valid = is_valid(board, num, position)
        print(str(valid))

        if valid:
            board_[row][col] = num

            if solve_board(board_):
                return True
            
            board_[row][col] = 0

    return False

def main():
    print_board(board)
    time.sleep(4)
    print("\n\n*_*_*_*_*_*_*_*_*_")
    solve_board(board)
    print("\n")
    print_board(board)

if __name__ == "__main__":
    main()
