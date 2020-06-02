def main():
    lenght = int(input("Enter the lenght of the river : "))
    breath = int(input("Enter the breath of the river : "))
    land = []
    print("Enter the land data : ")
    for y in range(lenght):
        land.append([])
        for _ in range(breath):
            land[y].append(int(input()))
        print("")
    print(land)            

if __name__ == "__main__":
    main()
