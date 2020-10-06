import random
b=input("Enter your choice:")
a=["rock","paper","scissor"]
p=random.randint(0,2)
c=a[p]
if c=="rock":
    if b==c:
        print("Tie")
    elif (b=="paper"):
        print("you have won")
    else:
        print("computer has won")
elif (c=="paper"):
    if b==c:
        print("tie")
    elif (b=="scissor"):
        print("you have won.")
    else:
        print("computer has won")
elif(c=="scissor"):
    if b==c:
        print("tie")
    elif(b=="rock"):
        print("b-player have won.")
    else:
        print("Opponent has won")
