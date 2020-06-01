
Board = [
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

def solve_board(board):
    position = find_nxt_empty(board)
    if not position:
        return True
    else:
        row, col = position

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num
            
            if solve_board(board):
                return True
            
            board[row][col] = 0
    
    return False

def is_valid(board, num, position):
    
    #checking row
    for col in range(len(board[0])):
        if ( (board[position[0]][col] == num) and (position[1] != col) ):
            return False
    
    #checking col
    for row in range(len(board)):
        if ( (board[row][position[1]] == num) and (position[0] != row) ):
            return False
    
    #checking boxes
    box_x = position[1] // 3
    box_y = position[0] // 3

    for row in range(box_y*3, box_y*3 +3):
        for col in range(box_x*3, box_x*3 +3):
            if ( (board[row][col] == num) and (position != (row, col) ) ):
                return False
    

    return True

def print_board(board):
    for row in range(len(board)):
        if ( (row % 3 == 0) and (row != 0) ):
            print("- - - - - - - - - - -")
        
        for col in range(len(board[0])):
            if ( (col % 3 == 0) and (col != 0) ):
                print("| ", end="")

            if (col == 8):
                print(board[row][col])
            else:
                print(f"{board[row][col]} ", end = "")

def find_nxt_empty(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if (board[row][col] == 0):
                return (row, col)
    return None

if __name__ == "__main__":
    print_board(Board)
    print("\n*_*_*_*_*_*_*_*_*_")
    print(solve_board(Board))
    print_board(Board)
