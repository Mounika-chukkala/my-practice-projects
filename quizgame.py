import random,quizdb
print("\nWelcome to the quiz...")
print()
score=0
questionno=0
db=quizdb.questions
que_list=[]
options=["a","b","c","d"]
que_no=0
que_asked=[]
answers=quizdb.answers
for i in range(len(db)):
    for j in db[i]:
        que_list.append(j)
while(questionno!=10):
    not_asked=False
    while(not_asked!=True):
        question=random.choice(que_list)
        if question not in que_asked:
            print(f"{questionno+1}.  {question}")
            que_asked.append(question)
            not_asked=True
    print()
    questionno+=1
    
    for i in range(len(db)):
        for j in db[i]:
            if(j==question):
                que_no=i
                for k in range(4):
                    print(f"{options[k]}) {db[i][j][k]}\n")
    print()
    answer=input("enter your option(A/B/C/D)").lower()
    print()
    if(answer==answers[que_no]):
        score+=1
        print(f"hurray !! Your answer is correct\n\n your current score is {score}/{questionno}\n\n")
    else:
        print(f"Your answer is wrong >>\n\n your current score is {score}/{questionno}\n")
        print(f"The correct answer is {answers[que_no]}")
print("Game is over ...thanks for playing \nBye bye have a nice day")
percent=(score/10)*100
print(f"Your total percentage is {percent}")
if(percent>50):
    print("You are good in python")
elif(percent>90):
    print("You are an expert in python")
else:
    print("Mundhu nerchukoni ra raa")