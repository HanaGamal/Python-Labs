num=int(input("enter a number: "))

for i in range(num):
    for j in range(num, -1, -1):
        if j > i:
            print(" ", end="")
        else:
            print("*", end="")
    print("")