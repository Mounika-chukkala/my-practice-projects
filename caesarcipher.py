# technique to send secret message
# in this the plain text will become cipher text
# plain text->cipher text |encryption
#cipher text ->plain text  |decryption
# e==(x+n)%26
# d==(x-n)%26
# if value becomes negative just add 26 to it
list2=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
a="yes"
while(a!="no"):
    dec=input("type 'encrypt' to encrypt the message or decrypt to decrypt the message:")
    dec.lower()
    shift=int(input("enter the shift:"))
    if(dec=="encrypt"):
        enc=input("enter the message you want to encrypt:")
        enc.lower()
        encmsg=""
        for i in enc:
            if i in list2:
                for j in range(len(list2)):
                    if(list2[j]==i):
                        break
                    # instead of the for loop above we can use list2.index(i) to get the position of the i in the list2
                    # index function is the inbuilt function
                    # to convert the char into it's ascii values we use ord function..like--> ord(h)
                num=(j+shift)%26
                if(num>=0):
                    encmsg+=list2[num]
                else:
                    encmsg+=list2[num+26]
            else:
                encmsg+=i
        print(f"your encrypeted message is \n {encmsg}")
    elif(dec=="decrypt"):
        des=input("enter the encrypted message you want to decrypt:")
        des.lower()
        desmsg=""
        for i in des:
            if i in list2:
                for j in range(len(list2)):
                    if(list2[j]==i):
                        break
                num=(j-shift)%26
                if(num>=0):
                    desmsg+=list2[num]
                else:
                    desmsg+=list2[num+26]
            else:
                desmsg+=i
        print(f"your decrypeted message is \n {desmsg}")
    else:
        print("enter the valid option!!!")
    a=input("do you want to encrypt/decrypt other messages(yes/no):")
    if(a=="no"):
        print("thank you for your time ...caeser cipher is closing now.....bye bye have a good day!!!")