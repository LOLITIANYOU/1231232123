import random
print("§--------------------------------Calculated Master--------------------------------§")
while True:
    coin=random.randint(1,4)
    if coin==1:        
        a=random.randint(10,20)
        b=random.randint(1,10)
        c=a+b
        user=input(str(a) + "+" + str(b) + "=")
        if str(c) == user:
            print("Congratulations, that's right")
        else:
            print("Wrong answer. The answer is"+str(c)+"，come on!")
    if coin==2:        
        a=random.randint(30,40)
        b=random.randint(1,10)
        c=a-b
        user=input(str(a) + "-" + str(b) + "=")
        if str(c) == user:
            print("Congratulations, that's right")
        else:

            print("Wrong answer. The answer is"+str(c)+"，come on!")
    if coin==3:        
        a=random.randint(10,20)
        b=random.randint(1,10)
        c=a*b
        user=input(str(a) + "*" + str(b) + "=")
        if str(c) == user:
            print("Congratulations, that's right")
        else:
            print("Wrong answer. The answer is"+str(c)+"，come on！")
    if coin==4:        
        a=random.randint(10,20)
        b=random.randint(1,10)
        c=a/b
        user=input(str(a) + "÷" + str(b) + "=")
        if str(c) == user:
            print("Congratulations, that's right")
        else:
            print("Wrong answer. The answer is"+str(c)+"，come on！")
