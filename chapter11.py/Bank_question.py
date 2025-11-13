class account:
    def __init__(self,balance,account_no):
        self.bal = balance
        self . acc = account_no

    def credit(self,amount):
        self.bal += amount
        print(f"Credit amount is {amount}")
        print(f"The acount balance is {self.total_balance()} ")
        
    def debit (self,amount):
        self.bal -= amount
        print(f"Debit amount is {amount}")
        print(f"The acount balance is {self.total_balance()} ")
        
    def total_balance(self):
        return self.bal
    

a = account(10000,12345) #Python me class ke andar function (method) ka order matter nahi karta,                
a.debit(1000)           #jab tak wo class define hone ke baad use ho raha hai.
a.credit(5000)
a.total_balance()
    
    