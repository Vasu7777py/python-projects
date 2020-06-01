
class ChessPices:
    Pice_id:str
    ColourOfPice:str

    def __init__(self, Pice_id, ColourOfPice):
        self.Pice_id = Pice_id
        self.ColourOfPice = ColourOfPice
    
    def get_pice_id(self):
        return(self.Pice_id)
    
    def get_ColourOfPice(self):
        return(self.ColourOfPice)

class King(ChessPices):
    Is_In_Check:bool
    Is_moved:bool

    def __init__(self, Pice_id, ColourOfPice):
        self.Pice_id = Pice_id
        self.ColourOfPice = ColourOfPice
        self.Is_In_Check = False
        self.Is_moved = False
    
    def is_moved(self):
        return self.Is_moved
    
    def is_in_check(self):
        return self.Is_In_Check

class Queen(ChessPices):
    def __init__(self, Pice_id, ColourOfPice):
        self.Pice_id = Pice_id
        self.ColourOfPice = ColourOfPice

class Bishop(ChessPices):
    def __init__(self, Pice_id, ColourOfPice):
        self.Pice_id = Pice_id
        self.ColourOfPice = ColourOfPice

class knight(ChessPices):
    def __init__(self, Pice_id, ColourOfPice):
        self.Pice_id = Pice_id
        self.ColourOfPice = ColourOfPice

class Rook(ChessPices):
    has_moved:bool
    def __init__(self, Pice_id, ColourOfPice):
        self.Pice_id = Pice_id
        self.ColourOfPice = ColourOfPice
        self.has_moved = False
    
    def is_moved(self):
        return self.has_moved

class Pawn(ChessPices):
    has_moved:bool
    def __init__(self, Pice_id, ColourOfPice):
        self.Pice_id = Pice_id
        self.ColourOfPice = ColourOfPice
        self.has_moved = False
    
    def is_moved(self):
        return self.has_moved

def Default_Pice_setup():
    Default_Pice_setup = {}
    White = {}
    Black = {}
    Default_Pice_setup["White"] = White
    Default_Pice_setup["Black"] = Black

    White["King"] = (King("King", "White"),(4,7))
    White["Queen"] = (Queen("Queen", "White"), (3,7))
    White["Bishop1"] = (Bishop("Bishop", "White"), (2,7))
    White["Bishop2"] = (Bishop("Bishop", "White"), (5,7))
    White["kinght1"] = (knight("knight", "White"), (1,7))
    White["kinght2"] = (knight("knight", "White"), (6,7))
    White["Rook1"] = (Rook("Rook", "White"), (0,7))
    White["Rook2"] = (Rook("Rook", "White"), (7,7))

    White["Pawn1"] = (Pawn("Pawn", "White"), (0,6))
    White["Pawn2"] = (Pawn("Pawn", "White"), (1,6))
    White["Pawn3"] = (Pawn("Pawn", "White"), (2,6))
    White["Pawn4"] = (Pawn("Pawn", "White"), (3,6))
    White["Pawn5"] = (Pawn("Pawn", "White"), (4,6))
    White["Pawn6"] = (Pawn("Pawn", "White"), (5,6))
    White["Pawn7"] = (Pawn("Pawn", "White"), (6,6))
    White["Pawn8"] = (Pawn("Pawn", "White"), (7,6))

    Black["King"] = (King("King", "Black"), (4,0))
    Black["Queen"] = (Queen("Queen", "Black"), (3,0))
    Black["Bishop1"] = (Bishop("Bishop", "Black"), (2,0))
    Black["Bishop2"] = (Bishop("Bishop", "Black"), (5,0))
    Black["kinght1"] = (knight("knight", "Black"), (1,0))
    Black["kinght2"] = (knight("knight", "Black"), (6,0))
    Black["Rook1"] = (Rook("Rook", "Black"), (0,0))
    Black["Rook2"] = (Rook("Rook", "Black"), (7,0))

    Black["Pawn1"] = (Pawn("Pawn", "Black"), (0,1))
    Black["Pawn2"] = (Pawn("Pawn", "Black"), (1,1))
    Black["Pawn3"] = (Pawn("Pawn", "Black"), (2,1))
    Black["Pawn4"] = (Pawn("Pawn", "Black"), (3,1))
    Black["Pawn5"] = (Pawn("Pawn", "Black"), (4,1))
    Black["Pawn6"] = (Pawn("Pawn", "Black"), (5,1))
    Black["Pawn7"] = (Pawn("Pawn", "Black"), (6,1))
    Black["Pawn8"] = (Pawn("Pawn", "Black"), (7,1))
    return Default_Pice_setup