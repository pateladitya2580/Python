from random import randint

class Trian :
    def __init__(self,train_no ):
        self.train_no = train_no
        
    def book (self,fro,to):
        print(f" The train {self.train_no} book from {fro} to {to}")
    def getstatus (self):
        print(f"The Train is runing on time no . is {self.train_no}")

    def getfair (self,fro,to):
        print(f" The fair is {randint(111,6666)} from {fro} to {to}")

Metro = Trian(11123)
Metro.book("jaipur" , "mumbai")
Metro.getstatus()
Metro.getfair("jaipur ", "mumbai")