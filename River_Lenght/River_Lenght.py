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

def main():
    lenght = int(input("Enter the lenght of the land : "))
    breath = int(input("Enter the breath of the land : "))
    land = np.ndarray(shape = (lenght, breath), dtype = int)
    for y in range(lenght):
        for x in range(breath):
            land_flag = False
            while not land_flag:
                land[y][x] = int(input(f"Enter the info of land {y}, {x} : "))
                if ((land[y][x] == 1) or (land[y][x] == 0)):
                    land_flag = True
                else:
                    print("Entered land info is not accetible")

    print(land)

if __name__ == "__main__":
    main()
