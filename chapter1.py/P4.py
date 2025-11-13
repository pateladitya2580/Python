import os

path = "C:\\Windows"  # Example folder

items = os.listdir(path)
print("Directory contents:")
for i in items:
    print(i)
