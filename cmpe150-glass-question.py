width = int(input())
height = int(input())
x = int(input())

change_of_water = 0

for a in range(x):
    change_of_water = change_of_water + int(input())
    filled = change_of_water // width
    add = change_of_water % width
    for i in range(height-filled-1):
        print("#", end="")
        for j in range(width):
            print(" ",end="")
        print("#")

    print("#", end="")
    for i in range(add):
        print("0",end="")
    for i in range(width-add):
        print(" ",end="")
    print("#")

    for i in range(filled):
        print("#",end="")
        for j in range(width):
            print("0",end="")
        print("#")

    for i in range(width+2):
        print("#", end="")

    print()


    for i in range(width+2):
        print("#", end="")

    print()