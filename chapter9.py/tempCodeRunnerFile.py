def generateTable(n):
    table = ""
    for i in range(1,11):
        table += f"{n}*{i}={n*i}\n"
    with open(f"./chapter9.py/tables.txt","w") as f:
        f.write(table)

for i in range(2,21):
    generateTable(i)