#1 for snake
#-1 for water
#0 for gun
import random

computer=random.choice([-1,0,1])
user=input("enter your choice: ")
userdict={
    "s":1,
    "w":-1,
    "g":0
}

reversedict={
    1:"snake",
    -1:"water",
    0:"gun"
}

usernum=userdict[user]

print(f"you chose {reversedict[usernum]}\nand computer chose {reversedict[computer]}")

if(computer==usernum):
    print("its a draw")
elif(computer==-1 and usernum==1):
    print("you win")
elif(computer==-1 and usernum==0):
    print("you lose")
elif(computer==1 and usernum==-1):
    print("you lose")
elif(computer==1 and usernum==0):
    print("you win")
elif(computer==0 and usernum==-1):
    print("you win")
elif(computer==0 and usernum==1):
    print("you lose")
else:
    print("something went wrong")