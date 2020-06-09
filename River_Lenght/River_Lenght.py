"""
QN:

Your given a 2d array of potentially unequal height and widht contaning only 0's and 1's.
Each represents land, and 1 represents part of a river. 
A river consists of any number of 1's that are either horizontal or vertically adjacent.
The number of adjacent 1's forming a river determine a river its size.

ex> 
[0, 0, 1, 1, 0, 1]
[0, 1, 1, 0, 1, 1]
[0, 0, 1, 1, 1, 0]
[0, 0, 0, 0, 0, 0]
[0, 1, 1, 0, 0, 0]
[1, 1, 1, 0, 0, 0]
"""

import numpy as np
from os import system

def create_Land(length, breath):
    land = np.ndarray(shape = (length, breath), dtype = int)
    for y in range(length):
        land_flag = False
        while not land_flag:
            land_data = input(f"Enter the info of the land : row {y} : ")
            if ((len(land_data) == breath )):
                for x in range(len(land_data)):
                    Area = int(land_data[x])
                    if ((Area != 1) and (Area != 0)):
                        print(f"in {Area}")
                        print(f"The entered info of the row {y} is wrong\ntry again")
                        break
                    else:
                        land[y][x] = Area
                else:
                    land_flag = True
            else:
                print("out")
                print(f"The entered info of the row {y} is wrong\ntry again")
    
    return land

class River:
    def __init__(self, land:np.ndarray, position:tuple):
        self.river_land = []
        self.Area = 0
        self.find_river_land(land, position)
    
    def find_river_land(self, land, position:tuple):
        self.river_land.append(position)
        self.Area += 1
        direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        for direct in direction:
            row = position[0] + direct[0]
            col = position[1] + direct[1]
            if River.is_inside_boundry(land, (row, col)):
                if ((land[row][col] == 1) and ((row, col) not in self.river_land)):
                    self.find_river_land(land, (row, col))
    
    @staticmethod
    def is_inside_boundry(land:np.ndarray, position: tuple):
        max_row, max_col = land.shape
        row, col = position
        if ((row >= max_row) or (col >= max_col)):
            return False
        else:
            return True

    def is_checked(self, position:tuple):
        if position in self.river_land:
            return True
        else:
            return False

def search_rivers(land):
    rivers = []
    for row in range(len(land)):
        for col in range(len(land[row])):
            if (land[row][col] == 1):
                is_checked = False
                for river in rivers:
                    is_checked = river.is_checked((row, col))
                    if is_checked:
                        break
                if not is_checked:
                    rivers.append(River(land, (row, col)))
    return rivers

def main():
    length = int(input("Enter the length of the land : "))
    breath = int(input("Enter the breath of the land : "))
    land = create_Land(length, breath)
    system("cls")
    rivers = search_rivers(land)
    print(land)
    for river in rivers:
        print(river.Area)

if __name__ == "__main__":
    main()
