import ChessPices

Tracker = [[],[],[],[],[],[],[],[]]

active = True
Waiting_For_Pice_Movement = False
selected = None

def start_Tracker():
    for x in range(8):
        y = 0
        while y < 8:
            value = {
                "Value": None,
                "State": not(active)
                }
            Tracker[x].append(value)
            y += 1

def start_set_up(Default_set:dict):
    start_Tracker()

    white, Black = Default_set["White"], Default_set["Black"]
    
    for key in white:
        value = white[key]
        obj = value[0]
        position = value[1]
        x, y = position[0], position[1]
        Tracker[x][y] = {
                "Value": "Value",
                "State": not(active),
                "Colour": "White",
                "object": obj
            }
    
    for key in Black:
        value = Black[key]
        obj = value[0]
        position = value[1]
        x, y = position[0], position[1]
        Tracker[x][y] = {
                "Value": "Value",
                "State": not(active),
                "Colour": "Black",
                "object": obj
            }

# Movement

def check_boundry(check:list):
    checked_positions = []
    for Move in check:
        x = Move[0]
        y = Move[1]
        if ((x >= 0) and (x < 8) and (y >= 0) and (y < 8)):
            checked_positions.append(Move)
    return checked_positions

# **************************************************************************************************************************

class PawnMoment:
    def check_spaces(self, curr_position:tuple, Is_Moved:bool, Pice_Colour:str):
        x, y = curr_position[0], curr_position[1]
        if Pice_Colour == "White":
            if Is_Moved:
                check_f = [(x, y -1)]
                check_d = [(x -1, y -1), (x +1, y -1)]
                checked_positions_f = check_boundry(check_f)
                checked_positions_d = check_boundry(check_d)
            else:
                check_f = [(x, y -1), (x, y -2)]
                check_d = [(x -1, y -1), (x +1, y -1)]
                checked_positions_f = check_boundry(check_f)
                checked_positions_d = check_boundry(check_d)
        else:
            if Is_Moved:
                check_f = [(x, y +1)]
                check_d = [(x -1, y +1), (x +1, y +1)]
                checked_positions_f = check_boundry(check_f)
                checked_positions_d = check_boundry(check_d)
            else:
                check_f = [(x, y +1), (x, y +2)]
                check_d = [(x -1, y +1), (x +1, y +1)]
                checked_positions_f = check_boundry(check_f)
                checked_positions_d = check_boundry(check_d)
        
        logicial_moves = []

        if len(checked_positions_f) != 0:
            for move in checked_positions_f:
                x1, y1 = move[0], move[1]
                value = Tracker[x1][y1]
                if value["Value"] == None:
                    logicial_moves.append(move)
        
        if len(checked_positions_d) != 0:
            for move in checked_positions_d:
                x1, y1 = move[0], move[1]
                value = Tracker[x1][y1]
                if value["Value"] != None:
                    values = Tracker[x1][y1]
                    colour = values["Colour"]
                    if (colour != Pice_Colour):
                        logicial_moves.append((x1, y1))

        return logicial_moves
    
    def move(self, Pawn:ChessPices.Pawn, position:tuple):
        Pawn.has_moved = True
        Colour = Pawn.ColourOfPice
        can_be_promoted = False
        if Colour == "White":
            if position == (position[0], 7):can_be_promoted = True
        else:
            if position == (position[0], 0):can_be_promoted = True
        if can_be_promoted:
            self.promotion(Colour, position)

    def promotion(self, Pice_Colour:str, position:tuple):
        
        pass

# **************************************************************************************************************************

class KnightMovement:
    def check_spaces(self, curr_position:tuple, Pice_Colour:str):
        x, y = curr_position[0], curr_position[1]
        #       up_left,        up_right,     right_up,      right_down,  down_right,  down_left,     left_up,      left_down
        check = [(x -1, y -2), (x +1, y -2), (x +2, y -1), (x +2, y +1), (x +1, y +2), (x -1, y +2), (x -2, y -1), (x -2, y +1)]
        checked_positions = check_boundry(check)
        
        logicial_moves = []
        for move in checked_positions:
            x1, y1 = move[0], move[1]
            value = Tracker[x1][y1]
            if value["Value"] != None:
                values = Tracker[x1][y1]
                colour = values["Colour"]
                if (colour != Pice_Colour):
                    logicial_moves.append((x1, y1))
            else:
                logicial_moves.append((x1, y1))
        return logicial_moves

    def move(self, Knight:ChessPices.knight):
        pass

# **************************************************************************************************************************

class BishopMovement:
    def check_spaces(self, curr_position:tuple, Pice_Colour:str):
        x, y = curr_position[0], curr_position[1]
        direction = [(1, 1), (1, -1), (-1, -1), (-1, +1)]
        logicial_moves = []
        for direc in direction:
            tempx = x
            tempy = y
            dead_end = False
            x_direc = direc[0]
            y_direc = direc[1]
            while not(dead_end):
                tempx = tempx + x_direc
                tempy = tempy + y_direc
                check = [(tempx, tempy)]
                checked_position = check_boundry(check)
                if len(checked_position) != 0:
                    move = checked_position[0]
                    x1, y1 = move[0], move[1]
                    value = Tracker[x1][y1]
                    if value["Value"] == None:
                        dead_end = False
                        logicial_moves.append(move)
                    else:
                        dead_end = True
                        colour = value["Colour"]
                        if Pice_Colour != colour:
                            logicial_moves.append(move)
                else:
                    dead_end = True
        return logicial_moves

    def move(self, Bishop:ChessPices.Bishop):
        pass
# **************************************************************************************************************************
class RookMoment:
    def check_spaces(self, curr_position:tuple, Pice_Colour:str):
        x, y = curr_position[0], curr_position[1]
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        logicial_moves = []
        for direc in direction:
            tempx = x
            tempy = y
            dead_end = False
            x_direc = direc[0]
            y_direc = direc[1]
            while not(dead_end):
                tempx = tempx + x_direc
                tempy = tempy + y_direc
                check = [(tempx, tempy)]
                checked_position = check_boundry(check)
                if len(checked_position) != 0:
                    move = checked_position[0]
                    x1, y1 = move[0], move[1]
                    value = Tracker[x1][y1]
                    if value["Value"] == None:
                        dead_end = False
                        logicial_moves.append(move)
                    else:
                        dead_end = True
                        colour = value["Colour"]
                        if Pice_Colour != colour:
                            logicial_moves.append(move)
                else:
                    dead_end = True
        return logicial_moves

    def move(self, Rook:ChessPices.Rook):
        Rook.has_moved = True

# **************************************************************************************************************************

class QueenMoments:
    def check_spaces(self, curr_position:tuple, Pice_Colour:str):
        x, y = curr_position[0], curr_position[1]
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, +1)]
        logicial_moves = []
        for direc in direction:
            tempx = x
            tempy = y
            dead_end = False
            x_direc = direc[0]
            y_direc = direc[1]
            while not(dead_end):
                tempx = tempx + x_direc
                tempy = tempy + y_direc
                check = [(tempx, tempy)]
                checked_position = check_boundry(check)
                if len(checked_position) != 0:
                    move = checked_position[0]
                    x1, y1 = move[0], move[1]
                    value = Tracker[x1][y1]
                    if value["Value"] == None:
                        dead_end = False
                        logicial_moves.append(move)
                    else:
                        dead_end = True
                        colour = value["Colour"]
                        if Pice_Colour != colour:
                            logicial_moves.append(move)
                else:
                    dead_end = True
        return logicial_moves

    def move(self, Queen:ChessPices.Queen):
        pass

# **************************************************************************************************************************

class KingMoment:
    def check_spaces(self, curr_position:tuple, Pice_Colour:str, has_moved:bool, is_in_check:bool):
        x, y = curr_position[0], curr_position[1]
        check = [(x, y -1), (x +1, y -1), (x +1, y), (x +1, y +1), (x, y +1), (x -1, y +1), (x -1, y), (x -1, y -1)]
        checked_positions = check_boundry(check)
        posible_moves = []
        logicial_moves = []
        for moves in checked_positions:
            x1, y1 = moves[0], moves[1]
            value = Tracker[x1][y1]
            if value["Value"] != None:
                colour = value["Colour"]
                if Pice_Colour != colour:
                    posible_moves.append(moves)
            else:posible_moves.append(moves)

        check_for_pices = ["King", "Pawn", "knight", "Rook", "Bishop", "Queen"]
        in_check_list = []
        for pice in check_for_pices:
            for move in posible_moves:
                is_in_check = False
                can_be_in_check = self.check_condition(pice, move, Pice_Colour, is_in_check)
                if can_be_in_check:
                    in_check_list.append(move)
            else:
                for move in in_check_list:
                    posible_moves.remove(move)
                else:in_check_list = []
        #castling_moves = self.castling(curr_position, Pice_Colour, has_moved, is_in_check)

        logicial_moves = posible_moves
        return logicial_moves
    
    def move(self, King:ChessPices.King):
        King.Is_moved = True

    def castling(self, curr_position:tuple, Pice_Colour:str, has_moved:bool, is_in_check:bool):
        y = curr_position[1]
        castling_moves = []
        if ( (not(has_moved)) and (not(is_in_check)) ):
            is_castling_posiable = True
            # King side
            for moves_in_x in range(5, 7):
                value = Tracker[moves_in_x][y]
                if value["Value"] != None:
                    is_castling_posiable = False
                else:
                    check_for_pices = ["King", "Pawn", "knight", "Rook", "Bishop", "Queen"]
                    for pice in check_for_pices:
                        is_in_check = False
                        can_be_in_check = self.check_condition(pice, (moves_in_x, y), Pice_Colour, is_in_check)
                        if can_be_in_check:
                            is_castling_posiable = False

            if is_castling_posiable:
                value = Tracker[7][y]
                if value["Value"] != None:
                    Colour = value["Colour"]
                    obj = value["object"]
                    if ( (Pice_Colour == Colour) and (obj.get_pice_id() == "Rook") ):
                        if not(obj.is_moved()):
                            castling_moves.append((7, y))


            # Queen side
            is_castling_posiable = True
            for moves_in_x in range(1, 4):
                value = Tracker[moves_in_x][y]
                if value["Value"] != None:
                    is_castling_posiable = False
                else:
                    check_for_pices = ["King", "Pawn", "knight", "Rook", "Bishop", "Queen"]
                    for pice in check_for_pices:
                        is_in_check = False
                        can_be_in_check = self.check_condition(pice, (moves_in_x, y), Pice_Colour, is_in_check)
                        if can_be_in_check:
                            is_castling_posiable = False

            if is_castling_posiable:
                value = Tracker[0][y]
                if value["Value"] != None:
                    Colour = value["Colour"]
                    obj = value["object"]
                    if ( (Pice_Colour == Colour) and (obj.get_pice_id() == "Rook") ):
                        if not(obj.is_moved()):
                            castling_moves.append((0, y))

        return castling_moves

    def check_condition(self, pice:str, move:tuple, Pice_Colour:str, is_in_check:bool):
        x, y = move[0], move[1]
        is_in_check = False
        if pice == "Pawn":
            if Pice_Colour == "White":
                direction = [(x -1, y -1), (x +1, y -1)]
            else:
                direction = [(x -1, y +1), (x +1, y +1)]
            is_in_check = self.is_in_check_def_short(direction, Pice_Colour, pice, is_in_check)

        elif pice == "knight":
            direction = [(x -1, y -2), (x +1, y -2), (x +2, y -1), (x +2, y +1), (x +1, y +2), (x -1, y +2), (x -2, y -1), (x -2, y +1)]
            is_in_check = self.is_in_check_def_short(direction, Pice_Colour, pice, is_in_check)

        elif pice == "Rook":
            direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            is_in_check = self.is_in_check_def_long(direction, Pice_Colour, move, pice, is_in_check)

        elif pice == "Bishop":
            direction = [(1, 1), (1, -1), (-1, -1), (-1, +1)]
            is_in_check = self.is_in_check_def_long(direction, Pice_Colour, move, pice, is_in_check)

        elif pice == "Queen":
            direction = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, +1)]
            is_in_check = self.is_in_check_def_long(direction, Pice_Colour, move, pice, is_in_check)

        elif pice == "King":
            direction = [(x, y -1), (x +1, y -1), (x +1, y), (x +1, y +1), (x, y +1), (x -1, y +1), (x -1, y), (x -1, y -1)]
            is_in_check = self.is_in_check_def_short(direction, Pice_Colour, pice, is_in_check)
        
        return is_in_check

    def is_in_check_def_short(self, direction:list, Pice_Colour:str, pice:str, is_in_check:bool):
        direction = check_boundry(direction)
        for moves in direction:
            value = Tracker[moves[0]][moves[1]]
            if value["Value"] != None:
                colour = value["Colour"]
                obj = value["object"]
                if ((Pice_Colour != colour) and (obj.get_pice_id() == pice)):
                    is_in_check = True
        return is_in_check
    
    def is_in_check_def_long(self, direction:list, Pice_Colour:str, move:tuple, pice:str, is_in_check:bool):
        x, y = move[0], move[1]
        for moves in direction:
                dead_end = False
                tempx = x
                tempy = y
                directionx = moves[0]
                directiony = moves[1]
                while not(dead_end):
                    tempx += directionx
                    tempy += directiony
                    check = [(tempx, tempy)]
                    check = check_boundry(check)
                    if len(check) != 0:
                        move_checked = check[0]
                        value = Tracker[move_checked[0]][move_checked[1]]
                        if value["Value"] != None:
                            colour = value["Colour"]
                            obj = value["object"]
                            #if ( (obj.get_pice_id() != "King") and (colour == Pice_Colour)):
                            if ((Pice_Colour == colour) and (obj.get_pice_id() == "King")):pass
                            else:dead_end = True
                            if ((Pice_Colour != colour) and (obj.get_pice_id() == pice)):
                                is_in_check = True
                    else:dead_end = True
        return is_in_check

# **************************************************************************************************************************

Pawn = PawnMoment()
Knight = KnightMovement()
Bishop = BishopMovement()
Rook = RookMoment()
Queen = QueenMoments()
King = KingMoment()

def find_posible_moves(position:tuple):
    x, y = position[0], position[1]
    logicial_moves = []
    pice = Tracker[x][y]
    if pice["Value"] != None:
        Colour = pice["Colour"]
        obj = pice["object"]
        pice_id = obj.get_pice_id()
        if pice_id == "Pawn":
            logicial_moves = Pawn.check_spaces(position, obj.is_moved(), Colour)
        if pice_id == "knight":
            logicial_moves = Knight.check_spaces(position, Colour)
        if pice_id == "Rook":
            logicial_moves = Rook.check_spaces(position, Colour)
        if pice_id == "Bishop":
            logicial_moves = Bishop.check_spaces(position, Colour)
        if pice_id == "Queen":
            logicial_moves = Queen.check_spaces(position, Colour)
        if pice_id == "King":
            logicial_moves = King.check_spaces(position, Colour, obj.is_moved(), obj.is_in_check())
    else:
        logicial_moves = []
    return logicial_moves

def Move_Pice(Selected_Pice_Position:tuple, To_Position:tuple, pice:str):
    fromX, fromY = Selected_Pice_Position[0], Selected_Pice_Position[1]
    toX, toY = To_Position[0], To_Position[1]
    
    if pice == "King":
        King.move(Tracker[fromX][fromY]["object"])
    elif pice == "Rook":
        Rook.move(Tracker[fromX][fromY]["object"])
    elif pice == "Pawn":
        Pawn.move(Tracker[fromX][fromY]["object"], To_Position)

    Tracker[toX][toY]["Value"] = Tracker[fromX][fromY]["Value"]
    Tracker[toX][toY]["State"] = Tracker[fromX][fromY]["State"]
    Tracker[toX][toY]["Colour"] = Tracker[fromX][fromY]["Colour"]
    Tracker[toX][toY]["object"] = Tracker[fromX][fromY]["object"]

    Tracker[Selected_Pice_Position[0]][Selected_Pice_Position[1]] = {
            "Value": None,
            "State": active
            }