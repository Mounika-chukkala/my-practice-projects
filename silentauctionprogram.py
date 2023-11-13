import os
amounts=[]
is_there_bidders="yes"
while(is_there_bidders!="no"):
    is_there_bidders=input("is there any bidders? (if yes type 'yes' else type 'no)")
    is_there_bidders.lower()
    if(is_there_bidders=="yes"):
        newbidder={}
        os.system('clear')
        print("****Welcome to silent auction***")
        name=input("What is your name?\n")
        bid_amt=int(input("whats is your bid amount?\n"))
        newbidder["name"]=name
        newbidder["bid amount"]=bid_amt
        amounts.append(newbidder)
    if(is_there_bidders=="no"):
        os.system('clear')
        print("so the auction is ended")
        a=input("do you want to see all the bid amounts(yes or no):").lower()
        if(a=="yes"):
            for i in range(len(amounts)):
                print(f'{amounts[i]["name"]}--->{amounts[i]["bid amount"]}')
        high=amounts[0]
        for i in range(len(amounts)):
            if(amounts[i]["bid amount"]>high["bid amount"]):
                high=amounts[i]
        print(f'highest bidder is {high["name"]} with the bid amount {high["bid amount"]}')
        print("Bye Bye")
        break