class calculater :
    def __init__(self,n):
        self.n = n
    
    def sqare(self):
        print(f"The sqare is {self.n*self.n}")
    @staticmethod
    def greet():
        print("Hello Aditya")
a = calculater(4)
a.sqare()
a.greet()
    