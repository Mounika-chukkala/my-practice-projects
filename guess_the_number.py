import random,os,logo
def level_choosen(num_choosen,attempts):
    print(f"you have {attempts} attempts to guess the number!!")
    while(attempts!=0):
        make_guess=int(input("Make a guess:\n"))
        if(make_guess>num_choosen):
            print("your guess is too high\nguess again")
        elif(make_guess<num_choosen):
            print("your guess is too low\nguess again")
        elif(make_guess==num_choosen):
            print("hurray!! your guess is correct ..\ncongrats")
            break
        attempts-=1
        print(f"you have {attempts} attempts remaining to guess the number!!")
        if(attempts==0):
            print("your attempts are completed and you couldn't guess the number")
            print("so sad !! but you lose):")
            break
play_again=True
while(play_again!=False):
    print(logo.logo)
    print("let me think of a number between 1 to 50")
    num_choosen=random.randint(1,50)
    level=input("choose level of difficulty...type 'easy' or 'medium' or 'hard':").lower()
    if(level=="easy"):
        level_choosen(num_choosen=num_choosen,attempts=10)
    elif(level=="medium"):
        level_choosen(num_choosen=num_choosen,attempts=5)
    elif(level=="hard"):
        level_choosen(num_choosen=num_choosen,attempts=3)
    else:
        print("Enter correct option ..it's an invalid one")
    wanna_play=input("do you want to play again...Type 'yes' or 'no':\n")
    if(wanna_play=="yes"):
        os.system('clear')
        play_again=True
    if(wanna_play=="no"):
        print("ok the game is closing...Bye Bye have a nice day (:")
        play_again=False