#90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F
mark = int(input("Enter your marks  "))
if(mark >=90 and mark <100):
    print("Ex")
elif(mark < 90 and mark >= 80 ):
    print("A")
else:
    print("Improve")