#F=(9/5×25)+32=45+32=77°F
def temperature(n):
    f = ((9/5)*n)+32
    return f

a = float(input("enter the temprature  "))

print(f"Tempreture in feranite is {temperature(a)} ")