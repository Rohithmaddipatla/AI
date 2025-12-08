import random

b = [" "]*9

def show():
    print(b[0:3],b[3:6],b[6:9])

def win(x):
    c=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),
       (1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(b[a]==b[c1]==b[d]==x for a,c1,d in c)

turn = "X"
while " " in b:
    show()
    if turn=="X":
        p=int(input("pos: "))
    else:
        p=random.choice([i for i in range(9) if b[i]==" "])
    b[p]=turn
    if win(turn):
        show()
        print(turn,"wins")
        break
    turn = "O" if turn=="X" else "X"
else:
    show()
    print("Draw")
