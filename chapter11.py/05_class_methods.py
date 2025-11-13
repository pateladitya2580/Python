class Employee:
    a = 1
    
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

e = Employee()
e.a = 45

e.show()

# @classmethod

# Ye decorator batata hai ki ye method class ke saath bind hai,
# na ki kisi particular object ke saath.

# Matlab — show() method class pe kaam karega,
# aur first parameter me class reference aayega (cls),
# not the object (self).
# yadi ye nahi hota too e.a = 45 show karta