import sys
u1=input("what is ur name?")
u2=input("what is ur name?")
u1_ans=input("%s,what do youwant")
u2_ans=input("%s,what do youwant")
def compare(u1,u2):
    if u1==u2:
        return("its tie")
    elif u1=="rock":
        if u2=="paper":
            return("u2 has won")
        elif u2=="scissor":
            return("u1 has won")
    elif u1=="paper":
        if u2=="rock":
            return("u1 has won")
        elif u2=="scissor":
            return("u2 has won")
    elif u1=="scissor":
        if u2=="rock":
            return("u2 has won")
        elif u2=="paper":
            return("u1 has won")
    else:
        return("plz. , return a valid statement")
        sys.exit()
print(compare(u1_ans,u2_ans))