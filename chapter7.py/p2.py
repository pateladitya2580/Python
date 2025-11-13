l = ["Harry", "Soham", "Sachin", "Rahul"]
for name in l:
    if(name.startswith("S")):
         print("Hello " ,name) #for loop list ke elements ko ek ek karke nikalta hai

                               #har element ka type wahi hota hai jo list me tha

                                #agar list me string hai → loop variable bhi string banega

                                 #agar list me number hai → loop variable number banega
for name in l:
     if(name.startswith("S")):
          print(f" Hello {name}")