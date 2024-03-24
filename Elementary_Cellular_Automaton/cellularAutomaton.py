from p5 import *
from time import sleep

celluleVivante = []
ancienneCellule = []
ecart = 50
lancement = False
etage = 0
rule = 110
print(bin(rule)[2:])

def rule0(lst):
    #000
    print("0")

def rule1():
    #001
    print("0")

def rule2():
    #010
    print("0")

def rule3():
    #011
    print("0")

def rule4():
    #100
    print("0")

def rule5():
    #101
    print("0")

def rule6():
    #110
    print("0")

def rule7():
    #111
    print("0")

rules = [rule0,rule1,rule2,rule3,rule4,rule5,rule6,rule7]

def multProche(val,mult):
    return (val//mult) * mult

def editeur():
    global ecart
    if mouse_is_pressed:
        celluleVivante.append((multProche(mouse_x,ecart),0))
        sleep(0.1)
    fill(0,255,0)
    rect(multProche(mouse_x,ecart),0,ecart,ecart)

def evolution():
    global celluleVivante, rule, rules
    for i,a in enumerate(bin(rule)[2:]):
        if a == "1":
            rules[i]() 

def setup():
    size(800,800)

def draw():
    global celluleVivante,lancement, etage
    background(255)
    if lancement == False:
        editeur()
    for i in range(len(celluleVivante)):
        fill(0)
        rect(celluleVivante[i][0],celluleVivante[i][1],ecart,ecart)
    if key == 'ENTER':
        lancement = not lancement
        evolution()
        sleep(0.1)



run()