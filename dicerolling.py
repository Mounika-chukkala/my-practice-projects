import random
def check():
    
        print("BYE BYE")
        print("thanks for rolling ,have a good day!!!")
print("Welcome to the Dice Rolling Stimulator")
a=input("press enter to roll the die(or q to quit:)")
if(a=='q'):
    check()
    exit(0)
else: 
    print(f"you rolled a {random.randint(1,6)} !")
while(a!='q'):
    a=(input("press ENTER to roll the dice again(or 'q' to quit):"))
    if(a=='q'):
        check()
        break
    else:
        m=random.randint(1,6)
        print(f"you rolled a {m} !")