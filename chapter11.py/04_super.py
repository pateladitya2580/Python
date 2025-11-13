class Employee:
    def __init__(self):
        print("constructor of employ")
    a = 1 

class Programmer(Employee):
    def __init__(self):
        print("constructor of programer")
    b = 2 

class Manager(Programmer):
    def __init__(self):
        super().__init__() # super se upar wala contructor chala warna individual chal te hai jiss class la usi me
        print("contructor of manager")
    c = 3

# o = Employee()
# print(o.a) 

# o = Programmer()
# print(o.a, o.b)


o = Manager()
print(o.a, o.b, o.c)