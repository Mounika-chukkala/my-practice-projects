your_name=input("enter your name:")
partner=input("enter your partner name:")
your_name.lower()
partner.lower()
name=your_name+partner
print(f"your name is {your_name} and your partner name is {partner}")
tr="true"
tr_val=0
for i in tr:
    for j in name:
        if(j==i):
            tr_val+=1
lo="love"
lo_val=0
for i in lo:
    for j in name:
        if (j==i):    
            lo_val+=1
total=(tr_val*10)+lo_val
print(f"you and your partner's love percentage is {total}%")
if(total>90):
    print("you are perfect pair ")
elif(70<total<90):
    print("you are good together")
elif(total<10):
    print("you may not the perfect pair..so sad")
else:
    print("you are alright together")
    