class Employ:
    salary = 120
    increment = 12
    
    @property

    def salary_increment(self):
        return(self.salary + self.salary*self.salary/100)
    
a = Employ()
print(a.salary_increment)