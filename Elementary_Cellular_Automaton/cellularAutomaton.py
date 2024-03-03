from p5 import *
from time import sleep

celluleVivante = []
ancienneCellule = []
ecart = 50
lancement = False
etage = 0
rule = 110
print(bin(rule)[2:])

def resolution():
    """metttre une pop up pour que l'utilisateur choissise la resolution de son ecran"""
    pass

def multProche(val,mult):
    return (val//mult) * mult

def editeur():
    global ecart, etage
    if mouse_is_pressed:
        celluleVivante.append((multProche(mouse_x,ecart),etage * ecart))
        sleep(0.1)
    fill(0,255,0)
    rect(multProche(mouse_x,ecart),etage * ecart,ecart,ecart)

def evolution():
    global celluleVivante, rule
    for a in ord(rule)[2:]:
        if i == 1:
            pass

def rule0():
    #000
    pass

def rule1():
    #001
    pass

def rule2():
    #010
    pass

def rule3():
    #011
    pass

def rule4():
    #100
    pass

def rule5():
    #101
    pass

def rule6():
    #110
    pass

def rule7():
    #111
    pass

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
        etage += 1 #changer a la fin des fonctions d'évolution, augmenter etage
        lancement = not lancement



run()