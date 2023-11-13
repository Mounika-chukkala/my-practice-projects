import random,higherlowerdatabase,logo
def comprint(c):
        name1=db_list[c]["name"]
        desc1=db_list[c]["desc"]
        country1=db_list[c]["country"]
        followers1=db_list[c]["followers"] 
        print(f'compare:\n{name1},{desc1} form {country1}')
        return followers1
not_out=True
score=0
print("let's start the game:")
print(logo.higherlower)
while(not_out!=False):
    db_list=higherlowerdatabase.higherlower
    if(score==0):
        comp1=random.randint(0,len(db_list)-1)
    f1=comprint(comp1)
    print(logo.vs)
    comp2=random.randint(0,len(db_list)-1)
    if(comp1==comp2):
        comp2=random.randint(0,len(db_list)-1)
    f2=comprint(comp2)
    answer=int(input("enter 1 if you think 1 has more followers else 2:\n"))
    if(answer==1):
        if(f1>=f2):
            print("you are correct")
            score+=1 
            print(f"your score is {score}")
        else:
            print(f"you lose with score {score}")
            not_out=False
            break
    elif(answer==2):
        if(f1<=f2):
            print("you are correct")
            score+=1 
            print(f"your score is {score}")
            print(comp1,comp2)
            comp1=comp2
            print(comp1,comp2)
        else:
            print(f"you lose with score {score}")
            not_out=False
            break
    else:
        not_out=False
        print(f"you lose with score {score}")
    
        