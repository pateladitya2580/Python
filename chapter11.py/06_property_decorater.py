# 🧠 Simple definition:

# @property ka use tab hota hai jab tum ek method ko attribute ki tarah access karna chahte ho — bina parentheses () lagaye.

# 🔍 Without @property:
class Employ:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

emp = Employ("Aditya", 10000)

print(emp.annual_salary())  # method call karne ke liye () zaruri hai


# ➡ Output:

# 120000

# ✅ With @property:
class Employ:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property
    def annual_salary(self):
        return self.salary * 12

emp = Employ("Aditya", 10000)

print(emp.annual_salary)  # ab attribute ki tarah access ho raha hai, method jaisa nahi


# ➡ Output:

# 120000

# 🔧 Samjho yeh kya karta hai:

# @property ek method ko read-only attribute bana deta hai.

# Tum usko () ke bina access kar sakte ho, jaise normal variable.

# Lekin andar ka logic method jaisa hi hota hai.