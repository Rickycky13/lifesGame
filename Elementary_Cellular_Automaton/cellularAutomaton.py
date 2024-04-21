from p5 import *
from time import sleep

celluleVivante = {}
width = 1920
ecart = 50
lancement = False
etage = 0
rule = 255
print(bin(rule)[2:])

def rule7(dico):
    #000
    newDico = {}
    for clef in dico.keys():
        if clef == -ecart or clef == multProche(width + ecart, ecart):
            continue 
        if dico[clef] == 0 and dico[clef - ecart] == 0 and dico[clef + ecart] == 0:
            newDico[clef] = 1
    return newDico

def rule6(dico):
    #001
    newDico = {}
    for clef in dico.keys():
        if clef == -ecart or clef == multProche(width + ecart, ecart):
            continue 
        if dico[clef] == 0 and dico[clef - ecart] == 0 and dico[clef + ecart] == 1:
            newDico[clef] = 1
    return newDico

def rule5(dico):
    #010
    newDico = {}
    for clef in dico.keys():
        if clef == -ecart or clef == multProche(width + ecart, ecart):
            continue 
        if dico[clef] == 1 and dico[clef - ecart] == 0 and dico[clef + ecart] == 0:
            newDico[clef] = 1
    return newDico

def rule4(dico):
    #011
    newDico = {}
    for clef in dico.keys():
        if clef == -ecart or clef == multProche(width + ecart, ecart):
            continue 
        if dico[clef] == 0 and dico[clef - ecart] == 1 and dico[clef + ecart] == 1:
            newDico[clef] = 1
    return newDico

def rule3(dico):
    #100
    newDico = {}
    for clef in dico.keys():
        if clef == -ecart or clef == multProche(width + ecart, ecart):
            continue 
        if dico[clef] == 0 and dico[clef - ecart] == 1 and dico[clef + ecart] == 0:
            newDico[clef] = 1
    return newDico

def rule2(dico):
    #101
    newDico = {}
    for clef in dico.keys():
        if clef == -ecart or clef == multProche(width + ecart, ecart):
            continue 
        if dico[clef] == 0 and dico[clef - ecart] == 1 and dico[clef + ecart] == 1:
            newDico[clef] = 1
    return newDico

def rule1(dico):
    #110
    newDico = {}
    for clef in dico.keys():
        if clef == -ecart or clef == multProche(width + ecart, ecart):
            continue 
        if dico[clef] == 1 and dico[clef - ecart] == 1 and dico[clef + ecart] == 0:
            newDico[clef] = 1
    return newDico

def rule0(dico):
    #111
    newDico = {}
    for clef in dico.keys():
        if clef == -ecart or clef == multProche(width + ecart, ecart):
            continue 
        if dico[clef] == 1 and dico[clef - ecart] == 1 and dico[clef + ecart] == 1:
            newDico[clef] = 1
    return newDico

rules = [rule0,rule1,rule2,rule3,rule4,rule5,rule6,rule7]

def multProche(val,mult):
    return (val//mult) * mult

def concatenation(lst):
    #recois une liste de dictionnaire et renvois un dictionnaire qui contient les positions de chacunes des cells vivantes
    print(lst)
    newDico = {}
    for i in range(-ecart,width+ecart,ecart):
        newDico[i] = 0
    for dico in lst:
        for clef,value in dico.items():
            if value == 1:
                newDico[clef] = 1
    return newDico

def editeur():
    global ecart
    if mouse_is_pressed:
        celluleVivante[multProche(mouse_x,ecart)] = 1
        sleep(0.1)
    fill(0,255,0)
    rect(multProche(mouse_x,ecart),0,ecart,ecart)

def evolution():
    global celluleVivante, rule, rules
    concateneur = []
    for i,a in enumerate(bin(rule)[2:]):
        if a == "1":
            concateneur.append(rules[i](celluleVivante))
    celluleVivante = concatenation(concateneur)

def setup():
    size(800,800)
    for i in range(-ecart,width+ecart,ecart):
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
        sleep(1)



run()