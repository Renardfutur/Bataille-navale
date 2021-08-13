import random


gril=[["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"]]
grilj=[["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"]]
grilr=[["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"]]
grilt=[["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"]]
long=len(gril)
num2=[1,2,3,4,5,6,7,8,9,10]
num=[0,1,2,3,4,5,6,7,8,9]
orien=["verticale","horizontale"]
bou=1

def plat():
    ca=1
    print("    A    B    C    D    E    F    G    H    I    J")
    i=1
    c=0
    while c<=9:
        print(ca,gril[i])
        ca+=1
        i+=1
        c+=1


def platr():
    ca=1
    print("    A    B    C    D    E    F    G    H    I    J")
    i=1
    c=0
    while c<=9:
        print(ca,gril[i])
        ca+=1
        i+=1
        c+=1

def platjr():
    ca=1
    print("    A    B    C    D    E    F    G    H    I    J")
    i=1
    c=0
    while c<=9:
        print(ca,vefj[i])
        ca+=1
        i+=1
        c+=1



plat()


#colpor=input("La collone de votre porte avion (5 cases)")
#ligpor=input("La ligne de votre porte avion (5 cases)")
#orpor=input("L'orientation?")

#colcroi=input("La collone de votre croiseur (4 cases)")
#ligcroi=input("La ligne de votre croiseur (4 cases)")
#orcroi=input("L'orientation?")

#colcont1=input("La collone de votre premier contre-torpilleur (3 cases)")
#ligcont1=input("La ligne de votre premier contre-torpilleur (3 cases)")
#orcont1=input("L'orientation?")

#colcont2=input("La collone de votre deuxième contre-torpilleur (3 cases)")
#ligcont2=input("La ligne de votre deuxième contre-torpilleur (3 cases)")
#orcont2=input("L'orientation?")

#colsous=input("La collone de votre sous marin (2 cases)")
#ligsous=input("La ligne de votre porte sous marin (2 cases)")
#orsous=input("L'orientation?")

#gril[lig+1][y]!=0 or gril[lig-1][y]!=0 or gril[lig+1][y+1]!=0 or gril[lig-1][y+1]!=0 or gril[lig+1][y+2]!=0 or gril[lig-1][y+2]!=0 or gril[lig+1][y+3]!=0 or gril[lig-1][y+3]!=0:




col=input("La collone de votre porte avion (5 cases)")
lig=int(input("La ligne de votre porte avion (5 cases)"))
ori=input("L'orientation?")
y=ord(col)
y=y-65
if ori=="horizontal":
    while lig<1 or lig>10 or y+5>10:
        print("hors champ")
        col=input("La collone de votre porte avion (4 cases)")
        lig=int(input("La ligne de votre porte avion (4 cases)"))
        ori=input("L'orientation?")
        y=ord(col)
        y=y-65
elif ori=="vertical":
    while lig<1 or lig+4>10 or y>10:
        print("hors champ")
        col=input("La collone de votre porte avion (4 cases)")
        lig=int(input("La ligne de votre porte avion (4 cases)"))
        ori=input("L'orientation?")
        y=ord(col)
        y=y-65

grilj[lig][y]="5"
gril[lig][y]="5"
portej=[]
portej.append(grilj[lig][y])


if ori=="vertical":
    for i in range(0,4):
        lig+=1
        grilj[lig][y]="5"
        gril[lig][y]="5"
        portej.append(grilj[lig][y])
elif ori=="horizontal":
    for i in range(0,4):
        y+=1
        grilj[lig][y]="5"
        gril[lig][y]="5"
        portej.append(grilj[lig][y])

print(portej)
plat()
col=input("La collone de votre croiseur (4 cases)")
lig=int(input("La ligne de votre croiseur (4 cases)"))
ori=input("L'orientation?")
y=ord(col)
y=y-65
print(y)
while bou==1:
    if ori=="horizontal":
        if y+3==9:
            if gril[lig+1][y]!="0" or gril[lig-1][y]!="0" or gril[lig+1][y+1]!="0" or gril[lig-1][y+1]!="0" or gril[lig+1][y+2]!="0" or gril[lig-1][y+2]!="0" or gril[lig+1][y+3]!="0" or gril[lig-1][y+3]!="0" or gril[lig][y-1]!="0" or gril[lig][y]!="0" or gril[lig][y+1]!="0" or gril[lig][y+2]!="0" or gril[lig][y+3]!="0" or gril[lig-1][y-1]!="0" or gril[lig-1][y+1]!="0":
                print("placement raté")
                col=input("La collone de votre croiseur (4 cases)")
                lig=int(input("La ligne de votre croiseur (4 cases)"))
                ori=input("L'orientation?")
                y=ord(col)
                y=y-65
            else:
                bou=0
        while y+3>9:
            col=input("Replacez la collone(4 cases)")
            lig = int(input("Replacez la ligne (4 cases)"))
            ori = input("L'orientation?")
            y=ord(col)
            y=y-65
        if y+3<9:
            if gril[lig+1][y]!="0" or gril[lig-1][y]!="0" or gril[lig+1][y+1]!="0" or gril[lig-1][y+1]!="0" or gril[lig+1][y+2]!="0" or gril[lig-1][y+2]!="0" or gril[lig+1][y+3]!="0" or gril[lig-1][y+3]!="0" or gril[lig][y-1]!="0" or gril[lig][y]!="0" or gril[lig][y+1]!="0" or gril[lig][y+2]!="0" or gril[lig][y+3]!="0" or gril[lig-1][y-1]!="0" or gril[lig+1][y-1]!="0" or gril[lig+1][y+4]!="0" or gril[lig-1][y+4]!="0":
                print("placement raté")
                col = input("Replacez la collone(4 cases)")
                lig=int(input("La ligne de votre croiseur (4 cases)"))
                ori=input("L'orientation?")
                print("loin")
                y = ord(col)
                y = y - 65
                print("pro")
            else:
                bou=0
    elif ori=="vertical":
        while lig+3>10 or lig<1:
            print("placement raté")
            col = input("Replacez la collone(4 cases)")
            lig = int(input("La ligne de votre croiseur (4 cases)"))
            ori = input("L'orientation?")
            y = ord(col)
            y = y - 65
        if lig+3<=10 and y!=9:
            if gril[lig][y+1]!="0" or gril[lig][y-1]!="0" or gril[lig+1][y+1]!="0" or gril[lig+1][y-1]!="0" or gril[lig+2][y+1]!="0" or gril[lig+2][y-1]!="0" or gril[lig+3][y-1]!="0" or gril[lig+3][y+1]!="0" or gril[lig-1][y]!="0" or gril[lig+4][y]!="0" or gril[lig+3][y]!="0" or gril[lig+2][y]!="0" or gril[lig+1][y]!="0" or gril[lig][y]!="0" or gril[lig-1][y-1]!="0" or gril[lig+4][y-1]!="0" or gril[lig-1][y+1]!="0" or gril[lig+4][y+1]!="0" :
                print("placement raté")
                col = input("Replacez la collone(4 cases)")
                lig = int(input("La ligne de votre croiseur (4 cases)"))
                ori = input("L'orientation?")
                y = ord(col)
                y = y - 65
            else:
                bou=0
        if lig+3<=10 and y==9:
            if gril[lig][y-1]!="0"or gril[lig+1][y-1]!="0" or gril[lig+2][y-1]!="0" or gril[lig+3][y-1]!="0" or gril[lig-1][y]!="0" or gril[lig+4][y]!="0" or gril[lig+3][y]!="0" or gril[lig+2][y]!="0" or gril[lig+1][y]!="0" or gril[lig][y]!="0" or gril[lig-1][y-1]!="0" or gril[lig+4][y-1]!="0" :
                print("placement raté")
                col = input("Replacez la collone(4 cases)")
                lig = int(input("La ligne de votre croiseur (4 cases)"))
                ori = input("L'orientation?")
                y = ord(col)
                y = y - 65
            else:
                bou=0



print("fin")
plat()
grilj[lig][y] = "4"
gril[lig][y] = "4"
croij=[grilj[lig][y]]

if ori == "vertical":
    for i in range(0,3):
        lig+=1
        grilj[lig][y]="4"
        gril[lig][y]="4"
        croij.append(grilj[lig][y])
elif ori == "horizontal":
    for i in range(0,3):
        y+=1
        grilj[lig][y]="4"
        gril[lig][y]="4"
        croij.append(grilj[lig][y])

bou=1
plat()
col=input("La collone de votre contre torpilleur (3 cases)")
lig=int(input("La ligne de votre contre torpilleur (3 cases)"))
ori=input("L'orientation?")
y=ord(col)
y=y-65
while bou==1:
    if ori=="horizontal":
        while y+2>9:
            print("placement raté")
            col = input("La collone de votre contre torpilleur (3 cases)")
            lig = int(input("La ligne de votre contre torpilleur (3 cases)"))
            ori = input("L'orientation?")
            y = ord(col)
            y = y - 65
        if y+2==9:
            if gril[lig+1][y]!="0" or gril[lig-1][y]!="0" or gril[lig+1][y+1]!="0" or gril[lig-1][y+1]!="0" or gril[lig+1][y+2]!="0" or gril[lig-1][y+2]!="0" or gril[lig][y-1]!="0" or gril[lig][y+1]!="0" or gril[lig-1][y-1]!="0" or gril[lig+1][y-1]!="0":
                print("placement raté")
                col=input("La collone de votre contre torpilleur (3 cases)")
                lig=int(input("La ligne de votre contre torpilleur (3 cases)"))
                ori=input("L'orientation?")
                y=ord(col)
                y=y-65
            else:
                bou=0
        if y+2<9:
            if gril[lig+1][y]!="0" or gril[lig-1][y]!="0" or gril[lig+1][y+1]!="0" or gril[lig-1][y+1]!="0" or gril[lig+1][y+2]!="0" or gril[lig-1][y+2]!="0" or gril[lig][y-1]!="0" or gril[lig][y+3]!="0" or gril[lig][y+1]!="0" or gril[lig-1][y-1]!="0" or gril[lig+1][y-1]!="0" or gril[lig+1][y+3]!="0" or gril[lig-1][y+3]!="0":
                print("placement raté")
                col=input("La collone de votre contre torpilleur (3 cases)")
                lig=int(input("La ligne de votre contre torpilleur (3 cases)"))
                ori=input("L'orientation?")
                y=ord(col)
                y=y-65
            else:
                bou=0
    elif ori=="vertical":
        while lig+2>10 or lig<1:
            print("placement raté")
            col = input("La collone de votre contre torpilleur (3 cases)")
            lig = int(input("La ligne de votre contre torpilleur (3 cases)"))
            ori = input("L'orientation?")
            y = ord(col)
            y = y - 65
        if lig+2<=10 and y!=9:
            if gril[lig][y+1]!="0" or gril[lig][y-1]!="0" or gril[lig+1][y+1]!="0" or gril[lig+1][y-1]!="0" or gril[lig+2][y+1]!="0" or gril[lig+2][y-1]!="0" or gril[lig-1][y]!="0" or gril[lig+3][y]!="0" or gril[lig+1][y]!="0" or gril[lig-1][y-1]!="0" or gril[lig-1][y+1]!="0" or gril[lig+3][y-1]!="0" or gril[lig+3][y+1]!="0":
                print("placement raté")
                col = input("La collone de votre contre torpilleur (3 cases)")
                lig = int(input("La ligne de votre contre torpilleur (3 cases)"))
                ori = input("L'orientation?")
                y = ord(col)
                y = y - 65
            else:
                bou=0
        if lig+2<=10 and y==9:
            if gril[lig][y-1]!="0" or gril[lig+1][y-1]!="0" or gril[lig+2][y-1]!="0" or gril[lig-1][y]!="0" or gril[lig+3][y]!="0" or gril[lig+1][y]!="0" or gril[lig-1][y-1]!="0" or gril[lig+3][y-1]!="0":
                print("placement raté")
                col = input("La collone de votre contre torpilleur (3 cases)")
                lig = int(input("La ligne de votre contre torpilleur (3 cases)"))
                ori = input("L'orientation?")
                y = ord(col)
                y = y - 65
            else:
                bou=0


plat()
grilj[lig][y]="3"
gril[lig][y]="3"
plat()
torj=[grilj[lig][y]]

if ori=="vertical":
    for i in range(0,2):
        lig+=1
        grilj[lig][y]="3"
        gril[lig][y]="3"
        torj.append(grilj[lig][y])
elif ori=="horizontal":
    for i in range(0,2):
        y+=1
        grilj[lig][y]="3"
        gril[lig][y]="3"
        torj.append(grilj[lig][y])

plat()

bou=1
col=input("La collone de votre contre torpilleur 2 (3 cases)")
lig=int(input("La ligne de votre contre torpilleur 2 (3 cases)"))
ori=input("L'orientation?")
y=ord(col)
y=y-65
print(y)

while bou==1:
    if ori=="horizontal":
        while y+2>9:
            print("placement raté")
            col = input("La collone de votre contre torpilleur 2(3 cases)")
            lig = int(input("La ligne de votre contre torpilleur 2(3 cases)"))
            ori = input("L'orientation?")
            y = ord(col)
            y = y - 65
        if y+2==9:
            if gril[lig+1][y]!="0" or gril[lig-1][y]!="0" or gril[lig+1][y+1]!="0" or gril[lig-1][y+1]!="0" or gril[lig+1][y+2]!="0" or gril[lig-1][y+2]!="0" or gril[lig][y-1]!="0" or gril[lig][y+1]!="0" or gril[lig-1][y-1]!="0" or gril[lig+1][y-1]!="0":
                print("placement raté")
                col=input("La collone de votre contre torpilleur 2(3 cases)")
                lig=int(input("La ligne de votre contre torpilleur 2(3 cases)"))
                ori=input("L'orientation?")
                y=ord(col)
                y=y-65
            else:
                bou=0
        if y+2<9:
            if gril[lig+1][y]!="0" or gril[lig-1][y]!="0" or gril[lig+1][y+1]!="0" or gril[lig-1][y+1]!="0" or gril[lig+1][y+2]!="0" or gril[lig-1][y+2]!="0" or gril[lig][y-1]!="0" or gril[lig][y+3]!="0" or gril[lig][y+1]!="0" or gril[lig-1][y-1]!="0" or gril[lig+1][y-1]!="0" or gril[lig+1][y+3]!="0" or gril[lig-1][y+3]!="0":
                print("placement raté")
                col=input("La collone de votre contre torpilleur 2(3 cases)")
                lig=int(input("La ligne de votre contre torpilleur 2(3 cases)"))
                ori=input("L'orientation?")
                y=ord(col)
                y=y-65
            else:
                bou=0
    elif ori=="vertical":
        while lig+2>10 or lig<1:
            print("placement raté")
            col = input("La collone de votre contre torpilleur 2(3 cases)")
            lig = int(input("La ligne de votre contre torpilleur 2(3 cases)"))
            ori = input("L'orientation?")
            y = ord(col)
            y = y - 65
        if lig+2<=10 and y!=9:
            if gril[lig][y+1]!="0" or gril[lig][y-1]!="0" or gril[lig+1][y+1]!="0" or gril[lig+1][y-1]!="0" or gril[lig+2][y+1]!="0" or gril[lig+2][y-1]!="0" or gril[lig-1][y]!="0" or gril[lig+3][y]!="0" or gril[lig+1][y]!="0" or gril[lig-1][y-1]!="0" or gril[lig-1][y+1]!="0" or gril[lig+3][y-1]!="0" or gril[lig+3][y+1]!="0":
                print("placement raté")
                col = input("La collone de votre contre torpilleur 2(3 cases)")
                lig = int(input("La ligne de votre contre torpilleur 2(3 cases)"))
                ori = input("L'orientation?")
                y = ord(col)
                y = y - 65
            else:
                bou=0
        if lig+2<=10 and y==9:
            if gril[lig][y-1]!="0" or gril[lig+1][y-1]!="0" or gril[lig+2][y-1]!="0" or gril[lig-1][y]!="0" or gril[lig+3][y]!="0" or gril[lig+1][y]!="0" or gril[lig-1][y-1]!="0" or gril[lig+3][y-1]!="0":
                print("placement raté")
                col = input("La collone de votre contre torpilleur 2(3 cases)")
                lig = int(input("La ligne de votre contre torpilleur 2(3 cases)"))
                ori = input("L'orientation?")
                y = ord(col)
                y = y - 65
            else:
                bou=0



grilj[lig][y]="1"
gril[lig][y]="1"
torj2=[grilj[lig][y]]

if ori=="vertical":
    for i in range(0,2):
        lig+=1
        grilj[lig][y]="1"
        gril[lig][y]="1"
        torj2.append(grilj[lig][y])
elif ori=="horizontal":
    for i in range(0,2):
        y+=1
        grilj[lig][y]="1"
        gril[lig][y]="1"
        torj2.append(grilj[lig][y])

plat()

bou=1
col=input("La collone de votre sous marin (2 cases)")
lig=int(input("La ligne de votre sous marin (2 cases)"))
ori=input("L'orientation?")
y=ord(col)
y=y-65
print(y)



while bou==1:
    if ori=="horizontal":
        while y+1>9:
            print("placement raté")
            col = input("La collone de votre contre sous-marin (2 cases)")
            lig = int(input("La ligne de votre contre sous-marin (2 cases)"))
            ori = input("L'orientation?")
            y = ord(col)
            y = y - 65
        if y+1==9:
            if gril[lig+1][y]!="0" or gril[lig-1][y]!="0" or gril[lig+1][y+1]!="0" or gril[lig-1][y+1]!="0" or gril[lig][y-1]!="0" or gril[lig][y+1]!="0" or gril[lig-1][y-1]!="0" or gril[lig+1][y-1]!="0":
                print("placement raté")
                col=input("La collone de votre contre sous-marin (2 cases)")
                lig=int(input("La ligne de votre contre sous-marin (2 cases)"))
                ori=input("L'orientation?")
                y=ord(col)
                y=y-65
            else:
                bou=0
        if y+1<9:
            if gril[lig+1][y]!="0" or gril[lig-1][y]!="0" or gril[lig+1][y+1]!="0" or gril[lig-1][y+1]!="0" or gril[lig][y-1]!="0" or gril[lig][y+1]!="0" or gril[lig-1][y-1]!="0" or gril[lig+1][y-1]!="0" or gril[lig-1][y+2]!="0" or gril[lig+1][y+2]!="0" or gril[lig][y+2]!="0":
                print("placement raté")
                col=input("La collone de votre contre sous-marin (2 cases)")
                lig=int(input("La ligne de votre contre sous-marin (2 cases)"))
                ori=input("L'orientation?")
                y=ord(col)
                y=y-65
            else:
                bou=0
    elif ori=="vertical":
        while lig+1>10 or lig<1:
            print("placement raté")
            col = input("La collone de votre contre sous-marin (2 cases)")
            lig = int(input("La ligne de votre contre sous-marin (2 cases)"))
            ori = input("L'orientation?")
            y = ord(col)
            y = y - 65
        if lig+1<=10 and y!=9:
            if gril[lig][y+1]!="0" or gril[lig][y-1]!="0" or gril[lig+1][y+1]!="0" or gril[lig+1][y-1]!="0" or gril[lig+2][y+1]!="0" or gril[lig+2][y-1]!="0" or gril[lig-1][y]!="0" or gril[lig+1][y]!="0" or gril[lig-1][y-1]!="0" or gril[lig-1][y+1]!="0" or gril[lig+2][y]!="0":
                print("placement raté")
                col = input("La collone de votre contre sous-marin (2 cases)")
                lig = int(input("La ligne de votre contre sous-marin (2 cases)"))
                ori = input("L'orientation?")
                y = ord(col)
                y = y - 65
            else:
                bou=0
        if lig+1<=10 and y==9:
            if gril[lig][y-1]!="0" or gril[lig+1][y-1]!="0" or gril[lig+2][y-1]!="0" or gril[lig-1][y]!="0" or gril[lig+1][y]!="0" or gril[lig-1][y-1]!="0" or gril[lig+2][y]!="0" or gril[lig][y]!="0":
                print("placement raté")
                col = input("La collone de votre contre sous-marin (2 cases)")
                lig = int(input("La ligne de votre contre sous-marin (2 cases)"))
                ori = input("L'orientation?")
                y = ord(col)
                y = y - 65
            else:
                bou=0



grilj[lig][y]="2"
gril[lig][y]="2"
sousj=[grilj[lig][y]]


if ori=="vertical":
    for i in range(0,1):
        lig+=1
        grilj[lig][y]="2"
        gril[lig][y]="2"
        sousj.append(grilj[lig][y])
elif ori=="horizontal":
    for i in range(0,1):
        y+=1
        grilj[lig][y]="2"
        gril[lig][y]="2"
        sousj.append(grilj[lig][y])

plat()

import random



def platr():
    ca=1
    print("    A    B    C    D    E    F    G    H    I    J")
    i=1
    c=0
    while c<=9:
        print(ca,grilr[i])
        ca+=1
        i+=1
        c+=1



bou=1
pos=random.choice(num2)
ran=random.choice(num)
ori=random.choice(orien)
print(pos,ran,ori)
pla=grilr[pos][ran]
while bou==1:
    if ori=="horizontale":
        while ran+4>9 or pos==0 or pos==11:
            pos = random.choice(num2)
            ran = random.choice(num)
            print(pos, ran, ori)
            platr()
        if ran+4<9:
            if grilr[pos][ran+1] != "0" or grilr[pos][ran+2] !="0" or grilr[pos][ran+3] != "0" or grilr[pos][ran+4] != "0"  or grilr[pos+1][ran]!="0" or grilr[pos-1][ran]!="0" or grilr[pos+1][ran+1]!="0" or grilr[pos-1][ran+1]!="0" or grilr[pos+1][ran+2]!="0" or grilr[pos-1][ran+2]!="0" or grilr[pos+1][ran+3]!="0"  or grilr[pos-1][ran+3]!="0" or grilr[pos+1][ran+4]!="0"  or grilr[pos-1][ran+4]!="0" or grilr[pos][ran-1]!="0" or grilr[pos][ran+5]!="0" or grilr[pos+1][ran-1]!="0" or grilr[pos-1][ran-1]!="0" or grilr[pos+1][ran+5]!="0" or grilr[pos-1][ran+5]!="0":
                pos = random.choice(num2)
                ran = random.choice(num)
                ori = random.choice(orien)
            else:
                bou=0
        if ran+4==9:
            if grilr[pos][ran+1] != "0" or grilr[pos][ran+2] != "0" or grilr[pos][ran+3] != "0" or grilr[pos][ran+4] != "0" or grilr[pos + 1][ran] != "0" or grilr[pos - 1][ran] != "0" or grilr[pos + 1][ran + 1] != "0" or grilr[pos - 1][ran + 1] != "0" or grilr[pos + 1][ran + 2] != "0" or grilr[pos - 1][ran + 2] != "0" or grilr[pos + 1][ran + 3] != "0" or grilr[pos - 1][ran + 3] != "0" or grilr[pos + 1][ran + 4] != "0" or grilr[pos - 1][ran + 4] != "0" or grilr[pos][ran - 1] != "0" or grilr[pos+1][ran-1]!="0" or grilr[pos-1][ran-1]!="0":
                pos = random.choice(num2)
                ran = random.choice(num)
                ori = random.choice(orien)
            else:
                bou = 0
    if ori=="verticale":
        while pos+4>10 or pos==0 or pos==11:
            pos = random.choice(num2)
            ran = random.choice(num)
            print(pos, ran, ori)
            platr()
        if pos+4<=10 and ran!=9:
            if grilr[pos+1][ran] != "0" or grilr[pos+2][ran] != "0" or grilr[pos+3][ran] != "0" or grilr[pos+4][ran+1]!="0" or grilr[pos][ran-1]!="0" or grilr[pos+1][ran+1]!="0" or grilr[pos+1][ran-1]!="0" or grilr[pos+2][ran+1]!="0" or grilr[pos+2][ran-1]!="0" or grilr[pos+3][ran+1]!="0"  or grilr[pos+3][ran-1]!="0" or grilr[pos-1][ran]!="0" or grilr[pos+4][ran-1]!="0" or grilr[pos+4][ran+1]!="0" or grilr[pos+5][ran]!="0" or grilr[pos-1][ran-1]!="0" or grilr[pos+5][ran-1]!="0" or grilr[pos+5][ran+1]!="0" or grilr[pos-1][ran+1]!="0":
                pos = random.choice(num2)
                ran = random.choice(num)
                ori = random.choice(orien)
            else:
                bou = 0
        if pos+4<=10 and ran==9:
            if grilr[pos+1][ran] != "0" or grilr[pos+2][ran] != "0" or grilr[pos+3][ran] != "0" or grilr[pos][ran-1]!="0" or grilr[pos+1][ran-1]!="0" or grilr[pos+2][ran-1]!="0" or grilr[pos+3][ran-1]!="0" or grilr[pos-1][ran]!="0" or grilr[pos+4][ran-1]!="0" or grilr[pos+5][ran]!="0" or grilr[pos-1][ran-1]!="0" or grilr[pos+5][ran-1]!="0":
                    pos = random.choice(num2)
                    ran = random.choice(num)
                    ori = random.choice(orien)
            else:
                bou =0


gril[pos][ran]="5"
grilr[pos][ran]="5"
porter=[grilr[pos][ran]]

if ori=="verticale":
    for i in range(0,4):
        pos+=1
        grilr[pos][ran]="5"
        gril[pos][ran]="5"
        porter.append(grilr[pos][ran])
elif ori=="horizontale":
    for i in range(0,4):
        ran+=1
        grilr[pos][ran]="5"
        gril[pos][ran]="5"
        porter.append(grilr[pos][ran])

platr()

pos=random.choice(num2)
ran=random.choice(num)
ori=random.choice(orien)
pla=grilr[pos][ran]
bou=1
while bou==1:
    if ori=="horizontale":
        while ran+3>9 or pos==0 or pos==11:
            pos = random.choice(num2)
            ran = random.choice(num)
            print(pos, ran, ori)
            platr()
        if ran+3==9:
            if grilr[pos][ran+1] != "0" or grilr[pos][ran+2] != "0" or grilr[pos][ran+3] != "0" or grilr[pos + 1][ran] != "0" or grilr[pos - 1][ran] != "0" or grilr[pos + 1][ran + 1] != "0" or grilr[pos - 1][ran + 1] != "0" or grilr[pos + 1][ran + 2] != "0" or grilr[pos - 1][ran + 2] != "0" or grilr[pos + 1][ran + 3] != "0" or grilr[pos - 1][ran + 3] != "0" or grilr[pos][ran - 1] != "0" or grilr[pos+1][ran-1] != "0" or grilr[pos-1][ran - 1] != "0":
                pos = random.choice(num2)
                ran = random.choice(num)
                ori = random.choice(orien)
            else:
                bou=0
        if ran+3<9:
            if grilr[pos][ran+1] != "0" or grilr[pos][ran+2] != "0" or grilr[pos][ran+3] != "0" or grilr[pos+1][ran]!="0" or grilr[pos-1][ran]!="0" or grilr[pos+1][ran+1]!="0" or grilr[pos-1][ran+1]!="0" or grilr[pos+1][ran+2]!="0" or grilr[pos-1][ran+2]!="0" or grilr[pos+1][ran+3]!="0"  or grilr[pos-1][ran+3]!="0" or grilr[pos][ran-1]!="0" or grilr[pos][ran+4]!="0" or grilr[pos - 1][ran + 4] != "0" or grilr[pos + 1][ran+4] != "0" or grilr[pos+1][ran-1] != "0" or grilr[pos-1][ran - 1] != "0":
                pos = random.choice(num2)
                ran = random.choice(num)
                ori = random.choice(orien)
            else:
                bou=0
        if ran==0:
            if grilr[pos][ran + 1] != "0" or grilr[pos][ran + 2] != "0" or grilr[pos][ran + 3] != "0" or grilr[pos + 1][ran] != "0" or grilr[pos - 1][ran] != "0" or grilr[pos + 1][ran + 1] != "0" or grilr[pos - 1][ran + 1] != "0" or grilr[pos + 1][ran + 2] != "0" or grilr[pos - 1][ran + 2] != "0" or grilr[pos + 1][ran + 3] != "0" or grilr[pos - 1][ran + 3] != "0" or grilr[pos][ran + 4] != "0" or grilr[pos - 1][ran + 4] != "0" or grilr[pos + 1][ran+4] != "0":
                pos = random.choice(num2)
                ran = random.choice(num)
                ori = random.choice(orien)
            else:
                bou=0
    if ori=="verticale":
        while pos+3>10:
            pos = random.choice(num2)
            ran = random.choice(num)
            print(pos, ran, ori)
            platr()
        if pos+3<=10 and ran!=9:
            if grilr[pos+1][ran] != "0" or grilr[pos+2][ran] != "0" or grilr[pos+3][ran] != "0" or grilr[pos][ran+1]!="0" or grilr[pos][ran-1]!="0" or grilr[pos+1][ran+1]!="0" or grilr[pos+1][ran-1]!="0" or grilr[pos+2][ran+1]!="0" or grilr[pos+2][ran-1]!="0" or grilr[pos+3][ran+1]!="0"  or grilr[pos+3][ran-1]!="0" or grilr[pos-1][ran]!="0" or grilr[pos+4][ran]!="0" or grilr[pos +4][ran -1] != "0" or grilr[pos + 4][ran+1] != "0" or grilr[pos - 1][ran+1] != "0" or grilr[pos-1][ran-1] != "0":
                pos = random.choice(num2)
                ran = random.choice(num)
                ori = random.choice(orien)
            else:
                bou=0
        if pos+3<=10 and ran==9:
            if grilr[pos+1][ran] != "0" or grilr[pos+2][ran] != "0" or grilr[pos+3][ran] != "0" or grilr[pos][ran-1]!="0" or grilr[pos+1][ran-1]!="0" or grilr[pos+2][ran-1]!="0" or grilr[pos+3][ran-1]!="0" or grilr[pos-1][ran]!="0" or grilr[pos+4][ran]!="0" or grilr[pos +4][ran -1] != "0" or grilr[pos-1][ran-1] != "0":
                pos = random.choice(num2)
                ran = random.choice(num)
                ori = random.choice(orien)
            else:
                bou=0



gril[pos][ran]="4"
grilr[pos][ran]="4"
croir=[grilr[pos][ran]]

if ori=="verticale":
    for i in range(0,3):
        pos+=1
        grilr[pos][ran]="4"
        gril[pos][ran]="4"
        croir.append(grilr[pos][ran])
elif ori=="horizontale":
    for i in range(0,3):
        ran+=1
        grilr[pos][ran]="4"
        gril[pos][ran]="4"
        croir.append(grilr[pos][ran])

platr()


pos=random.choice(num2)
ran=random.choice(num)
ori=random.choice(orien)
bou=1
print(pos,ran,ori)
pla=grilr[pos][ran]
while bou==1:
    if ori=="horizontale":
        if ran+2>9:
            pos = random.choice(num2)
            ran = random.choice(num)
            print(pos, ran, ori)
            platr()
        if ran+2<9:
            if grilr[pos][ran+1]!="0" or grilr[pos][ran+2]!="0" or grilr[pos+1][ran]!="0" or grilr[pos-1][ran]!="0" or grilr[pos+1][ran+1]!="0" or grilr[pos-1][ran+1]!="0" or grilr[pos+1][ran+2]!="0" or grilr[pos-1][ran+2]!="0" or grilr[pos][ran-1]!="0" or grilr[pos][ran+3]!="0" or grilr[pos +1][ran +3] != "0" or grilr[pos -1][ran+3] != "0" or grilr[pos + 1][ran-1] != "0" or grilr[pos-1][ran-1] != "0":
                pos = random.choice(num2)
                ran = random.choice(num)
                ori = random.choice(orien)
            else:
                bou=0
        if ran+2==9:
            if grilr[pos][ran+1]!="0" or grilr[pos][ran+2]!="0" or grilr[pos + 1][ran]!="0" or grilr[pos - 1][ran]!="0" or grilr[pos + 1][ran + 1]!="0" or grilr[pos - 1][ran + 1]!="0" or grilr[pos + 1][ran + 2]!="0" or grilr[pos - 1][ran + 2]!="0" or grilr[pos][ran - 1]!="0" or grilr[pos + 1][ran-1] != "0" or grilr[pos-1][ran-1] != "0":
                pos = random.choice(num2)
                ran = random.choice(num)
                ori = random.choice(orien)
            else:
                bou=0
        if ran==0:
            if grilr[pos][ran+1]!="0" or grilr[pos][ran+2]!="0" or grilr[pos+1][ran]!="0" or grilr[pos-1][ran]!="0" or grilr[pos+1][ran+1]!="0" or grilr[pos-1][ran+1]!="0" or grilr[pos+1][ran+2]!="0" or grilr[pos-1][ran+2]!="0" or grilr[pos][ran+3]!="0" or grilr[pos +1][ran +3] != "0" or grilr[pos -1][ran+3] != "0":
                pos = random.choice(num2)
                ran = random.choice(num)
                ori = random.choice(orien)
            else:
                bou=0
    if ori=="verticale":
        while pos+2>10:
            pos = random.choice(num2)
            ran = random.choice(num)
            print(pos, ran, ori)
            platr()
        if pos+2<=10 and ran!=9:
                if pos+2>10 or grilr[pos+1][ran]!="0" or grilr[pos+2][ran]!="0" or grilr[pos][ran+1]>"0" or grilr[pos][ran-1]!="0" or grilr[pos+1][ran+1]!="0" or grilr[pos+1][ran-1]!="0" or grilr[pos+2][ran+1]!="0" or grilr[pos+2][ran-1]!="0" or grilr[pos+3][ran]!="0" or grilr[pos-1][ran]!="0" or grilr[pos +3][ran +1] != "0" or grilr[pos+3][ran-1] != "0" or grilr[pos -1][ran +1] != "0" or grilr[pos -1][ran-1] != "0":
                    pos = random.choice(num2)
                    ran = random.choice(num)
                    ori = random.choice(orien)
                else:
                    bou=0
        if pos+2<=10 and ran==9:
                if pos+2>10 or grilr[pos+1][ran]!="0" or grilr[pos+2][ran]!="0" or grilr[pos][ran-1]!="0" or grilr[pos+1][ran-1]!="0" or grilr[pos+2][ran-1]!="0" or grilr[pos+3][ran]!="0" or grilr[pos-1][ran]!="0" or grilr[pos -1][ran -1] != "0" or grilr[pos +3][ran-1] != "0":
                    pos = random.choice(num2)
                    ran = random.choice(num)
                    ori = random.choice(orien)
                else:
                    bou=0



gril[pos][ran]="3"
grilr[pos][ran]="3"
torr=[grilr[pos][ran]]

if ori=="verticale":
    for i in range(0,2):
        pos+=1
        grilr[pos][ran]="3"
        gril[pos][ran]="3"
        torr.append(grilr[pos][ran])
elif ori=="horizontale":
    for i in range(0,2):
        ran+=1
        grilr[pos][ran]="3"
        gril[pos][ran]="3"
        torr.append(grilr[pos][ran])

platr()

pos=random.choice(num2)
ran=random.choice(num)
ori=random.choice(orien)
bou=1
print(pos,ran,ori)
pla=grilr[pos][ran]


while bou==1:
    if ori=="horizontale":
        if ran+2>9:
            pos = random.choice(num2)
            ran = random.choice(num)
            print(pos, ran, ori)
            platr()
        if ran+2<9:
            if grilr[pos][ran+1]!="0" or grilr[pos][ran+2]!="0" or grilr[pos+1][ran]!="0" or grilr[pos-1][ran]!="0" or grilr[pos+1][ran+1]!="0" or grilr[pos-1][ran+1]!="0" or grilr[pos+1][ran+2]!="0" or grilr[pos-1][ran+2]!="0" or grilr[pos][ran-1]!="0" or grilr[pos][ran+3]!="0" or grilr[pos +1][ran +3] != "0" or grilr[pos -1][ran+3] != "0" or grilr[pos + 1][ran-1] != "0" or grilr[pos-1][ran-1] != "0":
                pos = random.choice(num2)
                ran = random.choice(num)
                ori = random.choice(orien)
            else:
                bou=0
        if ran+2==9:
            if grilr[pos][ran+1]!="0" or grilr[pos][ran+2]!="0" or grilr[pos + 1][ran]!="0" or grilr[pos - 1][ran]!="0" or grilr[pos + 1][ran + 1]!="0" or grilr[pos - 1][ran + 1]!="0" or grilr[pos + 1][ran + 2]!="0" or grilr[pos - 1][ran + 2]!="0" or grilr[pos][ran - 1]!="0" or grilr[pos + 1][ran-1] != "0" or grilr[pos-1][ran-1] != "0":
                pos = random.choice(num2)
                ran = random.choice(num)
                ori = random.choice(orien)
            else:
                bou=0
        if ran==0:
            if grilr[pos][ran+1]!="0" or grilr[pos][ran+2]!="0" or grilr[pos+1][ran]!="0" or grilr[pos-1][ran]!="0" or grilr[pos+1][ran+1]!="0" or grilr[pos-1][ran+1]!="0" or grilr[pos+1][ran+2]!="0" or grilr[pos-1][ran+2]!="0" or grilr[pos][ran+3]!="0" or grilr[pos +1][ran +3] != "0" or grilr[pos -1][ran+3] != "0":
                pos = random.choice(num2)
                ran = random.choice(num)
                ori = random.choice(orien)
            else:
                bou=0
    if ori=="verticale":
        while pos+2>10:
            pos = random.choice(num2)
            ran = random.choice(num)
            print(pos, ran, ori)
            platr()
        if pos+2<=10 and ran!=9:
                if pos+2>10 or grilr[pos+1][ran]!="0" or grilr[pos+2][ran]!="0" or grilr[pos][ran+1]>"0" or grilr[pos][ran-1]!="0" or grilr[pos+1][ran+1]!="0" or grilr[pos+1][ran-1]!="0" or grilr[pos+2][ran+1]!="0" or grilr[pos+2][ran-1]!="0" or grilr[pos+3][ran]!="0" or grilr[pos-1][ran]!="0" or grilr[pos +3][ran +1] != "0" or grilr[pos+3][ran-1] != "0" or grilr[pos -1][ran +1] != "0" or grilr[pos -1][ran-1] != "0":
                    pos = random.choice(num2)
                    ran = random.choice(num)
                    ori = random.choice(orien)
                else:
                    bou=0
        if pos+2<=10 and ran==9:
                if pos+2>10 or grilr[pos+1][ran]!="0" or grilr[pos+2][ran]!="0" or grilr[pos][ran-1]!="0" or grilr[pos+1][ran-1]!="0" or grilr[pos+2][ran-1]!="0" or grilr[pos+3][ran]!="0" or grilr[pos-1][ran]!="0" or grilr[pos -1][ran -1] != "0" or grilr[pos +3][ran-1] != "0":
                    pos = random.choice(num2)
                    ran = random.choice(num)
                    ori = random.choice(orien)
                else:
                    bou=0


gril[pos][ran]="1"
grilr[pos][ran]="1"
torr2=[grilr[pos][ran]]

if ori=="verticale":
    for i in range(0,2):
        pos+=1
        grilr[pos][ran]="1"
        gril[pos][ran]="1"
        torr2.append(grilr[pos][ran])
elif ori=="horizontale":
    for i in range(0,2):
        ran+=1
        grilr[pos][ran]="1"
        gril[pos][ran]="1"
        torr2.append(grilr[pos][ran])

platr()


pos=random.choice(num2)
ran=random.choice(num)
ori=random.choice(orien)
print(pos,ran,ori)
pla=grilr[pos][ran]
bou=1

while bou==1:
    if ori=="horizontale":
        if ran+1>9:
            pos = random.choice(num2)
            ran = random.choice(num)
            print(pos, ran, ori)
        if ran+1<9:
            if pla!="0" or grilr[pos][ran+1]!="0" or grilr[pos+1][ran]!="0" or grilr[pos-1][ran]!="0" or grilr[pos+1][ran+1]!="0" or grilr[pos-1][ran+1]!="0" or grilr[pos][ran+2]!="0" or grilr[pos][ran-1]!="0" or grilr[pos+1][ran+2]!="0" or grilr[pos-1][ran+2]!="0" or grilr[pos-1][ran-1]!="0" or grilr[pos+1][ran-1]!="0":
                pos = random.choice(num2)
                ran = random.choice(num)
                ori = random.choice(orien)
                print(pos, ran, ori,"mop")
                platr()
            else:
                bou=0
        if ran+1==9:
            if pla != "0" or grilr[pos][ran+1]!="0" or grilr[pos + 1][ran]!="0" or grilr[pos - 1][ran]!="0" or grilr[pos + 1][ran + 1]!="0" or grilr[pos - 1][ran + 1]!="0" or grilr[pos][ran - 1]!="0" or grilr[pos-1][ran-1]!="0" or grilr[pos+1][ran-1]!="0":
                pos = random.choice(num2)
                ran = random.choice(num)
                ori = random.choice(orien)
                print(pos, ran, ori,"ois")
                platr()
            else:
                bou=0
        if ran==0:
            if pla!="0" or grilr[pos][ran+1]!="0" or grilr[pos+1][ran]!="0" or grilr[pos-1][ran]!="0" or grilr[pos+1][ran+1]!="0" or grilr[pos-1][ran+1]!="0" or grilr[pos][ran+2]!="0" or grilr[pos][ran-1]!="0" or grilr[pos-1][ran-1]!="0" or grilr[pos+1][ran-1]!="0":
                pos = random.choice(num2)
                ran = random.choice(num)
                ori = random.choice(orien)
                print(pos, ran, ori,"grue")
                platr()
            else:
                bou=0
    if ori=="verticale":
        if pos+1>10:
            pos = random.choice(num2)
            ran = random.choice(num)
            print(pos, ran, ori,"rert")
        if pos+1<=10 and ran!=9:
            if pla!="0" or grilr[pos+1][ran]!="0" or grilr[pos][ran+1]!="0" or grilr[pos][ran-1]!="0" or grilr[pos+1][ran+1]!="0" or grilr[pos+1][ran-1]!="0" or grilr[pos+2][ran]!="0" or grilr[pos-1][ran]!="0" or grilr[pos-1][ran-1]!="0" or grilr[pos-1][ran+1]!="0" or grilr[pos+2][ran-1]!="0" or grilr[pos+2][ran+1]!="0":
                    pos = random.choice(num2)
                    ran = random.choice(num)
                    ori = random.choice(orien)
                    print(pos, ran, ori,"teyu")
                    platr()
            else:
                bou=0
        if ran==9 and pos+1<=10:
            if pla!="0" or grilr[pos+1][ran]!="0" or grilr[pos][ran-1]!="0" or grilr[pos+1][ran-1]!="0" or grilr[pos+2][ran]!="0" or grilr[pos-1][ran]!="0" or grilr[pos-1][ran-1]!="0" or grilr[pos+2][ran-1]!="0":
                    pos = random.choice(num2)
                    ran = random.choice(num)
                    ori = random.choice(orien)
                    print(pos, ran, ori,"kame")
                    platr()
            else:
                bou=0

gril[pos][ran]="2"
grilr[pos][ran]="2"
sousr=[grilr[pos][ran]]


if ori=="verticale":
        pos+=1
        grilr[pos][ran]="2"
        gril[pos][ran]="2"
        sousr.append(grilr[pos][ran])
elif ori=="horizontale":
        ran+=1
        grilr[pos][ran]="2"
        gril[pos][ran]="2"
        sousr.append(grilr[pos][ran])

detr=["0","0","0","0","0"]
detr1=["0","0","0","0"]
detr2=["0","0","0"]
detr3=["0","0"]
platr()



tour=0
jeu=1
nb=0
nbr=0
platr()
scor=25
scoj=25

soj=0
croj=0
porj=0
toj=0
toj2=0

sor=0
cror=0
porr=0
tor=0
tor2=0

situ=0
vefr=[["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"]]
vefj=[["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0"]]


triche=input("Avec triche=oui, sans triche=non")



if triche=="oui":
    while jeu==1:
        if tour==0:
            colt = input("La collone de votre tir")
            ligt = int(input("La ligne de votre tir"))
            yt=ord(colt)
            yt=yt-65
            print("au joueur")
            platj()
            if grilr[ligt][yt]!="0":
                if grilr[ligt][yt]=="5":
                    print("touché")
                    porj=porj+1
                    colmar = input("La collone de votre marqueur X")
                    ligmar = int(input("La ligne de votre marqueur X"))
                    ym = ord(colmar)
                    ym = ym - 65
                    vefj[ligmar][ym] = "X"
                    grilr[ligt][yt] == "0"
                    if porj==5:
                        print("Coulé")
                        nb+=1
                if grilr[ligt][yt]=="4":
                    print("touché")
                    croj = croj + 1
                    colmar = input("La collone de votre marqueur X")
                    ligmar = int(input("La ligne de votre marqueur X"))
                    ym = ord(colmar)
                    ym = ym - 65
                    vefj[ligmar][ym] = "X"
                    grilr[ligt][yt] == "0"
                    if croj == 4:
                        print("Coulé")
                        nb += 1
                if grilr[ligt][yt]=="3":
                    print("touché")
                    toj = toj + 1
                    colmar = input("La collone de votre marqueur X")
                    ligmar = int(input("La ligne de votre marqueur X"))
                    ym = ord(colmar)
                    ym = ym - 65
                    vefj[ligmar][ym] = "X"
                    grilr[ligt][yt] == "0"
                    if toj == 3:
                        print("Coulé")
                        nb += 1
                if grilr[ligt][yt]=="1":
                    print("touché")
                    toj2 = toj2 + 1
                    colmar = input("La collone de votre marqueur X")
                    ligmar = int(input("La ligne de votre marqueur X"))
                    ym = ord(colmar)
                    ym = ym - 65
                    vefj[ligmar][ym] = "X"
                    grilr[ligt][yt] == "0"
                    if toj2 == 3:
                        print("Coulé")
                        nb += 1
                if grilr[ligt][yt]=="2":
                    print("touché")
                    soj = soj + 1
                    colmar = input("La collone de votre marqueur X")
                    ligmar = int(input("La ligne de votre marqueur X"))
                    ym = ord(colmar)
                    ym = ym - 65
                    vefj[ligmar][ym] = "X"
                    grilr[ligt][yt] == "0"
                    if soj == 2:
                        print("Coulé")
                        nb += 1
            elif grilr[ligt][yt]=="0":
                print("Raté pour le joueur")
                colmar = input("La collone de votre marqueur o")
                ligmar = int(input("La ligne de votre marqueur o"))
                ym = ord(colmar)
                ym = ym - 65
                vefj[ligmar][ym] = "o"
                tour=1
        scoj=scoj-1
        platjr()
        if nb==5:
            print("Le joueur a gagné")
            jeu=0
            break
        if scoj==0:
            print("Vous étes à cours de point, l'ordinateur a gagné")
            jeu=0
            break
        if tour==1:
            print("à l'ordinateur à gagné")
            pos = random.choice(num2)
            ran = random.choice(num)
            while grilj[pos][ran]=="X" or grilj[pos][ran]=="o":
                pos = random.choice(num2)
                ran = random.choice(num)
            print("L'ordinateur va tirer sur",pos,chr(ran+65))
            reponse = str(input("Touché,coulé ou raté"))
            if reponse=="raté":
                print("Raté pour l'ordi")
                grilj[pos][ran] = "o"
                tour = 0
            if reponse=="touché" or reponse=="coulé":
                if grilj[pos][ran] == "0":
                    grilj[pos][ran] == "X"
                    tour=0
                if grilj[pos][ran]!="0":
                    if grilj[pos][ran]=="5":
                        porr+=1
                        grilj[pos][ran] == "X"
                        if porr==5:
                            nbr+=1
                    if grilj[pos][ran]=="4":
                        cror += 1
                        grilj[pos][ran] == "X"
                        if porr == 4:
                            nbr += 1
                    if grilj[pos][ran]=="3":
                        torj= torj+1
                        grilj[pos][ran] == "X"
                        if torj == 3:
                            nbr += 1
                    if grilj[pos][ran]=="1":
                        torj2 += 1
                        grilj[pos][ran] == "X"
                        if torj2 == 3:
                            nbr += 1
                    if grilj[pos][ran]=="2":
                        sor += 1
                        grilj[pos][ran] == "X"
                        if sor == 2:
                            nbr += 1
        scor=scor-1
        if nbr==5:
            print("L'ordinateur a gagné")
            jeu=0
            break
        if scor==0:
            print("Le joueur a gagné")
            jeu=0
            break
if triche=="non":
    while jeu==1:
        if tour==0:
            colt = input("La collone de votre tir")
            ligt = int(input("La ligne de votre tir"))
            yt=ord(colt)
            yt=yt-65
            print("au joueur")
            platj()
            if grilr[ligt][yt]!="0":
                if grilr[ligt][yt]=="5":
                    print("touché")
                    porj=porj+1
                    colmar = input("La collone de votre marqueur X")
                    ligmar = int(input("La ligne de votre marqueur X"))
                    ym = ord(colmar)
                    ym = ym - 65
                    vefj[ligmar][ym] = "X"
                    grilr[ligt][yt] == "0"
                    situ=1
                    if porj==5:
                        print("Coulé")
                        nb+=1
                        situ = 2
                if grilr[ligt][yt]=="4":
                    print("touché")
                    croj = croj + 1
                    colmar = input("La collone de votre marqueur X")
                    ligmar = int(input("La ligne de votre marqueur X"))
                    ym = ord(colmar)
                    ym = ym - 65
                    vefj[ligmar][ym] = "X"
                    grilr[ligt][yt] == "0"
                    situ = 1
                    if croj == 4:
                        print("Coulé")
                        nb += 1
                        situ = 2
                if grilr[ligt][yt]=="3":
                    print("touché")
                    toj = toj + 1
                    colmar = input("La collone de votre marqueur X")
                    ligmar = int(input("La ligne de votre marqueur X"))
                    ym = ord(colmar)
                    ym = ym - 65
                    vefj[ligmar][ym] = "X"
                    grilr[ligt][yt] == "0"
                    situ = 1
                    if toj == 3:
                        print("Coulé")
                        nb += 1
                        situ = 2
                if grilr[ligt][yt]=="1":
                    print("touché")
                    toj2 = toj2 + 1
                    colmar = input("La collone de votre marqueur X")
                    ligmar = int(input("La ligne de votre marqueur X"))
                    ym = ord(colmar)
                    ym = ym - 65
                    vefj[ligmar][ym] = "X"
                    grilr[ligt][yt] == "0"
                    situ = 1
                    if toj2 == 3:
                        print("Coulé")
                        nb += 1
                        situ = 2
                if grilr[ligt][yt]=="2":
                    print("touché")
                    soj = soj + 1
                    colmar = input("La collone de votre marqueur X")
                    ligmar = int(input("La ligne de votre marqueur X"))
                    ym = ord(colmar)
                    ym = ym - 65
                    vefj[ligmar][ym] = "X"
                    grilr[ligt][yt] == "0"
                    situ = 1
                    if soj == 2:
                        print("Coulé")
                        nb += 1
                        situ = 2
            elif grilr[ligt][yt]=="0":
                print("Raté pour le joueur")
                colmar = input("La collone de votre marqueur o")
                ligmar = int(input("La ligne de votre marqueur o"))
                ym = ord(colmar)
                ym = ym - 65
                vefj[ligmar][ym] = "o"
                situ = 3
                tour=1
        scoj=scoj-1
        platjr()
        if nb==5:
            print("Le joueur a gagné")
            jeu=0
            break
        if scoj==0:
            print("L'ordinateur a gagné")
            jeu=0
            break
        if tour==1:
            print("à l'ordianteur")
            pos = random.choice(num2)
            ran = random.choice(num)
            while grilj[pos][ran]=="X" or grilj[pos][ran]=="o":
                pos = random.choice(num2)
                ran = random.choice(num)
            print("L'ordinateur va tirer sur",pos,chr(ran+65))
            reponse=input("Touché,coulé ou raté")
            if grilj[pos][ran]!="0":
                if grilj[pos][ran]=="5":
                    porr+=1
                    grilj[pos][ran] == "X"
                    situ=1
                    if porr==5:
                        nbr+=1
                        situ = 2
                if grilj[pos][ran]=="4":
                    cror += 1
                    grilj[pos][ran] == "X"
                    situ = 1
                    if porr == 4:
                        nbr += 1
                        situ = 2
                if grilj[pos][ran]=="3":
                    torj= torj+1
                    grilj[pos][ran] == "X"
                    situ = 1
                    if torj == 3:
                        nbr += 1
                        situ = 2
                if grilj[pos][ran]=="1":
                    torj2 += 1
                    grilj[pos][ran] == "X"
                    situ = 1
                    if torj2 == 3:
                        nbr += 1
                        situ = 2
                if grilj[pos][ran]=="2":
                    sor += 1
                    grilj[pos][ran] == "X"
                    situ = 1
                    if sor == 2:
                        nbr += 1
                        situ = 2
            elif grilj[pos][ran]=="0":
                situ = 3
                tour=0
            while situ == 3 and reponse != "raté":
                print("Menteur")
                reponse = input("touché,coulé ou raté")
            while situ == 1 and reponse != "touché":
                print("Menteur")
                reponse = input("touché,coulé ou raté")
            while situ == 2 and reponse != "coulé":
                print("Menteur")
                reponse = input("touché,coulé ou raté")
        scor=scor-1
        if nbr==5:
            print("L'ordinateur a gagné")
            jeu=0
            break
        if scor==0:
            print("Le joueur a gagné")
            jeu=0
            break



