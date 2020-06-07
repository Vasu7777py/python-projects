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
[0, 1, 0, 0, 0, 0]
[0, 1, 0, 0, 0, 0]
[1, 1, 1, 0, 0, 0]
"""

import numpy as np
from os import system

def create_Land(length, breath):
    land = np.ndarray(shape = (length, breath), dtype = int)
    for y in range(length):
        for x in range(breath):
            land_flag = False
            while not land_flag:
                land[y][x] = int(input(f"Enter the info of land {y}, {x} : "))
                if ((land[y][x] == 1) or (land[y][x] == 0)):
                    land_flag = True
                else:
                    print("Entered land info is not a valid entry,\nEnter the correct value : ")
    
    return land

class River:
    def __init__(self):
        self.river_land = []
        self.length = 0
    
    def find_river_land(self, land, position:tuple):
        self.river_land.append(position)
        self.length += 1
        direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        for direct in direction:
            row = position[0] + direct[0]
            col = position[1] + direct[1]
            if ((land[row][col] == 1) and ((row, col) not in self.river_land)):
                self.find_river_land(land, (row, col))
    
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
                if (len(rivers) == 0):
                    river = River()
                    river.find_river_land(land, (row, col))
                    rivers.append(river)
                else:
                    for river in rivers:
                        if river.is_checked((row, col)):
                            break
                    else:
                        river = River()
                        river.find_river_land(land, (row, col))
                        rivers.append(river)
    return rivers

def main():
    length = int(input("Enter the length of the land : "))
    breath = int(input("Enter the breath of the land : "))
    land = create_Land(length, breath)
    system("cls")
    rivers = search_rivers(land)
    print(land, rivers)

if __name__ == "__main__":
    main()
