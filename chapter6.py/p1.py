a = int(input("enter 1 no. "))
b = int(input("enter 2 no. "))
c = int(input("enter 3 no. "))
d = int(input("enter 4 no. "))

if( a>b and a>c and a>d):
    print("gretest no . is  ", a)
elif(b>a and b>c and b>d):
    print("greatest no. is  ",b)
elif(c>a and c>b and c>d):
    print("greatest no. is  ",c)
else:
    print("greatest no. is  ",d)