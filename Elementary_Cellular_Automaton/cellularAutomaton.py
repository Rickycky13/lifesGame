from p5 import *
from time import sleep

celluleVivante = {}
ecart = 50
lancement = False
etage = 0
rule = 255
print(bin(rule)[2:])

def rule0(dico):
    #000
    newDico = {}
    for clef in dico.keys():
        if dico[clef] == 0 and dico[clef - ecart] == 0 and dico[clef + ecart] == 0:
            newDico[clef] == 1
    return newDico

def rule1(dico):
    #001
    newDico = {}
    for clef in dico.keys():
        if dico[clef] == 0 and dico[clef - ecart] == 0 and dico[clef + ecart] == 1:
            newDico[clef] == 1
    return newDico

def rule2(dico):
    #010
    newDico = {}
    for clef in dico.keys():
        if dico[clef] == 1 and dico[clef - ecart] == 0 and dico[clef + ecart] == 0:
            newDico[clef] == 1
    return newDico

def rule3(dico):
    #011
    newDico = {}
    for clef in dico.keys():
        if dico[clef] == 1 and dico[clef - ecart] == 0 and dico[clef + ecart] == 1:
            newDico[clef] == 1
    return newDico

def rule4(dico):
    #100
    newDico = {}
    for clef in dico.keys():
        if dico[clef] == 0 and dico[clef - ecart] == 1 and dico[clef + ecart] == 0:
            newDico[clef] == 1
    return newDico

def rule5(dico):
    #101
    newDico = {}
    for clef in dico.keys():
        if dico[clef] == 0 and dico[clef - ecart] == 1 and dico[clef + ecart] == 1:
            newDico[clef] == 1
    return newDico

def rule6(dico):
    #110
    newDico = {}
    for clef in dico.keys():
        if dico[clef] == 1 and dico[clef - ecart] == 1 and dico[clef + ecart] == 0:
            newDico[clef] == 1
    return newDico

def rule7(dico):
    #111
    newDico = {}
    for clef in dico.keys():
        if dico[clef] == 1 and dico[clef - ecart] == 1 and dico[clef + ecart] == 1:
            newDico[clef] == 1
    return newDico

rules = [rule0,rule1,rule2,rule3,rule4,rule5,rule6,rule7]

def multProche(val,mult):
    return (val//mult) * mult

def editeur():
    global ecart
    if mouse_is_pressed:
        celluleVivante[multProche(mouse_x,ecart)] = 1
        sleep(0.1)
    fill(0,255,0)
    rect(multProche(mouse_x,ecart),0,ecart,ecart)

def evolution():
    global celluleVivante, rule, rules
    newCell = {}
    for i,a in enumerate(bin(rule)[2:]):
        if a == "1":
            newCell += rules[i](celluleVivante)

def setup():
    size(800,800)
    for i in range(0,1080,ecart):
        celluleVivante[i] = 0

def draw():
    global celluleVivante,lancement, etage
    background(255)
    if lancement == False:
        editeur()
    for clef in celluleVivante.keys():
        if celluleVivante[clef] == 1:
            fill(0)
            rect(clef,etage,ecart,ecart)
    if key == 'ENTER':
        lancement = not lancement
        evolution()
        etage += ecart
        sleep(0.1)



run()