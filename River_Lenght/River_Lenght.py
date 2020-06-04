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
