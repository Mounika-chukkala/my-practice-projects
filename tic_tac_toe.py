list2=["zero","one","two","three","four","five","six","seven","eight"]
checker=0
def printboard(XState,ZState):
    for i in range(len(list2)):
        list2[i]='X' if XState[i] else ('O' if ZState[i] else i+1)
    print()
    print(f"\t | {list2[0]} | {list2[1]} | {list2[2]} |")
    print( "\t-|---|---|---|-")
    print(f"\t | {list2[3]} | {list2[4]} | {list2[5]} |")
    print( "\t-|---|---|---|-")
    print(f"\t | {list2[6]} | {list2[7]} | {list2[8]} |")
    print()
def checkwin(XState,ZState):
    xwins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in xwins:
        if sum(XState[win[0]],XState[win[1]],XState[win[2]])==3:
            print("X is the winner")
            return 1
        if sum(ZState[win[0]],ZState[win[1]],ZState[win[2]])==3:
            print("O is the winner")
            return 0

            
    return -1
def sum(a,b,c):
    sum=a+b+c
    return sum
print("Welcome to tic tac toe game...")
turn=1
XState=[0,0,0,0,0,0,0,0,0]
ZState=[0,0,0,0,0,0,0,0,0]
while(True):
    printboard(XState,ZState)
    if(turn==1):
        print("x's Chance")
        value=int(input("enter your choice: "))
        if(ZState[value-1]!=1 and XState[value-1]!=1):
            XState[value-1]=1
            
        else:
            print("Make another choice ..that slot is already filled..")
            value=int(input("enter your choice: "))
            XState[value-1]=1
        checker+=1
    else:
        print("O's Chance")
        value=int(input("Enter your choice: "))
        if(ZState[value-1]!=1 and XState[value-1]!=1):
            ZState[value-1]=1
        else:
            print("Make another choice ..that slot is already filled..")
            value=int(input("enter your choice: "))
            ZState[value-1]=1
        checker+=1
    if(checker==9):
        print("game is over ..all blocks are full and no way to continue the game..So sorry play again.!!  :(")
        break
    if(checkwin(XState,ZState)!=-1):
        printboard(XState,ZState)
        print("Match over")
        break
    turn =1-turn#1-0=1 and 1-1=0

    
