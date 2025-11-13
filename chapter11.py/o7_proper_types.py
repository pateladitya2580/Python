# 🧠 Simple Definition:

# @property, @<name>.getter, @<name>.setter, aur @<name>.deleter — ye sab encapsulation ke tools hain.
# Ye tumhe control dete hain ki:

# koi variable kaise read ho (getter)

# kaise change ho (setter)

# kaise delete ho (deleter)

# 🔹 Step 1: Normal case (without property)
class Employ:
    def __init__(self, salary):
        self.salary = salary

a = Employ(10000)
print(a.salary)      # direct access
a.salary = -5000     # koi validation nahi, galat bhi chalega!


# ➡ Problem: koi restriction nahi. Negative salary bhi assign ho gayi 😑

# 🔹 Step 2: Using property + setter (correct way)
class Employ:
    def __init__(self, salary):
        self._salary = salary     # underscore = private variable

    @property
    def salary(self):             # ✅ GETTER — jab hum value read karte hain
        return self._salary

    @salary.setter
    def salary(self, value):      # ✅ SETTER — jab hum value set karte hain
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value

        # 🔹 raise ValueError kya hota hai?

# raise Python ka keyword hai jo janbujhkar ek error generate (throw) karta hai 
# — jab tumhe lagta hai user ya program ne galat data diya hai.
# ValueError ek built-in error type hai jo tab use hota hai jab value logically sahi nahi hoti,
#  lekin datatype sahi hota hai.

a = Employ(10000)
print(a.salary)      # calls the getter → returns 10000

a.salary = 15000     # calls the setter → sets 15000
print(a.salary)

a.salary = -2000     # ❌ error raise hoga


# ➡ Output:

# 10000
# 15000
# ValueError: Salary cannot be negative

# 🔍 Breakdown:
# Decorator	Use	Trigger hota hai jab...
# @property	Getter method	Tum variable read karte ho
# @<name>.setter	Setter method	Tum variable assign karte ho
# @<name>.deleter	Deleter method	Tum variable delete karte ho (del obj.attr)

# “value” actually wo nayi value hoti hai jo tum attribute ko assign kar rahe ho.
# Matlab jab bhi tum obj.salary = something likhte ho, Python automatically us 
# something ko setter ke andar value ke naam se pass karta hai.