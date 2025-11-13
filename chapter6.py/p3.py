p1 ="Make a lot of money"
p2 ="buy now"
p3 ="subscribe this"
p4 ="click this"

msg = input(" enter your sentance   ")
if( p1 in msg or p2 in msg or p3 in msg or p4 in msg):
    print("This is spam")
else:
    print("This is not spam")