marks1 = int(input("enter first subjet marks "))
marks2 = int(input("enter second subjet marks "))
marks3 = int(input("enter third  subjet marks "))

total_percentage = (100*(marks1 + marks2 + marks3)/300)

if(total_percentage >= 40 and marks1 >= 33 and marks2 >= 33 and marks3 >=  33):
    print("you are pass " , total_percentage)
else:
    print("Reexam ",total_percentage)
