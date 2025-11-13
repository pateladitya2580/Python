n = int(input("enter the no "))
for i in range(2,n+1):
    if(n%i == 0 ):
        print("This is not prime")
        break
    else:
        print("This no. is prime")
        break