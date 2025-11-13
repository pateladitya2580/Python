try:
    with open("poem_p1_.txt", "r") as f:
        content = f.read()

    if "twinkle" in content:
        print("Yes")
    else:
        print("No")

except :
    print("File not found! Please check the file name or path.")
