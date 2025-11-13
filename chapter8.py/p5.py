def patern(n):
    for i in range(0,n):
        print("*"*(n-i),end="")
        print("")
n = int(input(" enter the value of n "))
patern(n)