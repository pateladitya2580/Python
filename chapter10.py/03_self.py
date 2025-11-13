class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod 
    def greet():
        print("Good morning")


harry = Employee()
# harry.language = "JavaScript" # This is an instance attribute
harry.greet()
harry.getInfo() 
# Employee.getInfo(harry)
 

#  🔹 @staticmethod kya karta hai:

# @staticmethod ka matlab hai — ye function class ke andar to likha hai,
# lekin ye class ya object ke kisi variable (self, cls, etc.) ko use nahi karta.

# Matlab:

# Ye sirf normal function ki tarah behave karta hai.

# Isko object se bhi call kar sakte ho (harry.greet())
# ya class se bhi (Employee.greet()).

# Iske andar self likhne ki zarurat nahi hoti, kyunki ye object ka data use nahi karta.


# 🔍 Ab yahan pe kya hua:

# Jab tum harry.getInfo() likhte ho,
# Python automatically convert karta hai isko:

# Employee.getInfo(harry)


# Matlab: class ka function call hua, aur harry object usme as argument gaya.

# Isliye function ke andar tumhe self likhna padta hai,
# taki function samjhe kis object ka data use karna hai.