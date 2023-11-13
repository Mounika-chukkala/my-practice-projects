import random
print("let's play hangman game...")
print("you have only 6 lives so try to guess the word in 6 attempts!! good luck buddy>>>")
comp_score=0
list1=[]
word=['devi','mounika','nitin','kabaddi','coding','chitti','love','radhakrishna','bhajan']
que=(random.choices(word))
que=str(que[0])
# print(que)
# print(len(que))
for i in range(len(que)):
    list1.append('_')
print(list1)
comp_score=0
for j in range(0,9):
    for i in range(0,6):
        if(i==5):
            print("*",end="")
        elif(j==0 or j==8):
            print("*",end="")
        elif(i==2 and j==1):
            print("+",end="")
        else:
            print(" ",end="")
    print() 
while(comp_score<=6):
    a=input("guess a letter:")
    if(a in que):
        print("hurray!!your guess is correct")
        for i in range(len(que)+1):
            if(que[i-1]==a):
                list1[i-1]=a
    else:
        comp_score+=1
        print("so sad!!Your guess is wrong")
    if(comp_score==0):
        for j in range(0,9):
            for i in range(0,6):
                if(i==5):
                    print("*",end="")
                elif(j==0 or j==8):
                    print("*",end="")
                elif(i==2 and j==1):
                    print("+",end="")
                else:
                    print(" ",end="")
            print()
        print ("You still have 6 chances left")
    elif(comp_score==1):
        for j in range(0,9):
            for i in range(0,6):
                if(i==5):
                    print("*",end="")
                elif(j==0 or j==8):
                    print("*",end="")
                elif(i==2 and j==1):
                    print("+",end="")
                elif(i==2 and j==2):
                    print("O",end="")
                else:
                    print(" ",end="")
            print() 
        print("you are left with 5 chances")
    elif(comp_score==2):
        for j in range(0,9):
            for i in range(0,6):
                if(i==5):
                    print("*",end="")
                elif(j==0 or j==8):
                    print("*",end="")
                elif(i==2 and j==1):
                    print("+",end="")
                elif(i==2 and j==2):
                    print("O",end="")
                elif(i==2 and (j==3 or j==4)):
                    print("|",end="")
                else:
                    print(" ",end="")
            print()
        print("you are left with 4 chances")
    elif(comp_score==3):
        for j in range(0,9):
            for i in range(0,6):
                if(i==5):
                    print("*",end="")
                elif(j==0 or j==8):
                    print("*",end="")
                elif(i==2 and j==1):
                    print("+",end="")
                elif(i==2 and j==2):
                    print("O",end="")
                elif(i==2 and (j==3 or j==4)):
                    print("|",end="")
                elif(j==3 and (i==3)):
                    print("\\",end="")
                else:
                    print(" ",end="")
            print()
        print("you are left with 3 more chances")
    elif(comp_score==4):
        for j in range(0,9):
            for i in range(0,6):
                if(i==5):
                    print("*",end="")
                elif(j==0 or j==8):
                    print("*",end="")
                elif(i==2 and j==1):
                    print("+",end="")
                elif(i==2 and j==2):
                    print("O",end="")
                elif(i==2 and (j==3 or j==4)):
                    print("|",end="")
                elif(j==3 and (i==3)):
                    print("\\",end="")
                elif(j==3 and i==1):
                    print("/",end="")
                else:
                    print(" ",end="")
            print()
        print("you are left with 2 more chances")
    elif(comp_score==5):
            for j in range(0,9):
                for i in range(0,6):
                    if(i==5):
                        print("*",end="")
                    elif(j==0 or j==8):
                        print("*",end="")
                    elif(i==2 and j==1):
                        print("+",end="")
                    elif(i==2 and j==2):
                        print("O",end="")
                    elif(i==2 and (j==3 or j==4)):
                        print("|",end="")
                    elif(j==3 and (i==3)):
                        print("\\",end="")
                    elif(j==3 and i==1):
                        print("/",end="")
                    elif(j==5 and i==3):
                        print("\\",end="")
                    else:
                        print(" ",end="")
                print()
            print("you have only one chance left")
    elif(comp_score==6):
        for j in range(0,9):
            for i in range(0,6):
                if(i==5):
                    print("*",end="")
                elif(j==0 or j==8):
                    print("*",end="")
                elif(i==2 and j==1):
                    print("+",end="")
                elif(i==2 and j==2):
                    print("O",end="")
                elif(i==2 and (j==3 or j==4)):
                    print("|",end="")
                elif(j==3 and (i==3)):
                    print("\\",end="")
                elif(j==3 and i==1):
                    print("/",end="")
                elif(j==5 and i==3):
                    print("\\",end="")
                elif(j==5 and i==1):
                    print("/",end="")
                else:
                    print(" ",end="")
            print()
        print("you lost the game man!!!---try again buddy")
        break
    print(list1)
    if('_' not in list1):
        print("you won buddyyy!!!congrats ~~~")
        break
print(f"The word is {que}")
print("bye bye")
