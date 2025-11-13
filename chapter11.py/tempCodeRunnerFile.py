class Employ:
    def __init__(self,name,salary,increment):
        self.na = name
        self.sa = salary
        self.inc = increment
        
    def show (self):
        print(self.na,self.sa,self.inc)

a = Employ("Aditya",120000,12)
b = Employ("Parag",130000,14)
a.show()
b.show()