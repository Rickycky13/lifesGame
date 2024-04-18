"""il faut transformer ce ficher en utils (enlever setup et draw, ramner sur une fonction global)"""


from p5 import *
from time import sleep

ecart = 25
celluleVivante = []
lancement = False




def setup():
    global testus
    size(800,800)
    fill(0)


############################################################################################################################################################


def multProche(val,mult):
    return (val//mult) * mult

def add8voisins(pos):
    global voisins, ecart
    voisins.append((multProche(pos[0],ecart)+ecart,multProche(pos[1],ecart)))
    voisins.append((multProche(pos[0],ecart),multProche(pos[1],ecart)+ecart))
    voisins.append((multProche(pos[0],ecart)+ecart,multProche(pos[1],ecart)+ecart))
    voisins.append((multProche(pos[0],ecart)-ecart,multProche(pos[1],ecart)))
    voisins.append((multProche(pos[0],ecart),multProche(pos[1],ecart)-ecart))
    voisins.append((multProche(pos[0],ecart)-ecart,multProche(pos[1],ecart)-ecart))
    voisins.append((multProche(pos[0],ecart)+ecart,multProche(pos[1],ecart)-ecart))
    voisins.append((multProche(pos[0],ecart)-ecart,multProche(pos[1],ecart)+ecart))
    
def countPos(lst):
    dict = {}
    for item in lst:
        if item in dict:
            dict[item]+=1
        else:
            dict[item] = 1
    return dict

def rules(dict,cellule):
    lst = []
    for key, value in dict.items():
        if value == 3:
            lst.append(key)
        elif value == 2 and key in cellule:
            lst.append(key)
    return lst

def evolution():
    """ fonction a activer dans draw qui s'occupe de toute l'évolution avec les trois règles"""
    global celluleVivante, voisins
    voisins = []
    for cell in celluleVivante:
        add8voisins(cell)
    nouvelleCellule= rules(countPos(voisins),celluleVivante)
    celluleVivante = nouvelleCellule

def editeur():
    global celluleVivante, ecart
    if mouse_is_pressed:
        celluleVivante.append((multProche(mouse_x,ecart),multProche(mouse_y,ecart)))
        sleep(0.1)
    fill(0,255,0)
    rect(multProche(mouse_x,ecart),multProche(mouse_y,ecart),ecart,ecart)

 
#####################################################################################################################################################################################


def draw():
    global celluleVivante, ecart, lancement
    background(255)
    if lancement == True:
        evolution()
        sleep(0.1)
    elif lancement == False:
        editeur()
    for i in range(len(celluleVivante)):
        fill(0)
        rect(celluleVivante[i][0],celluleVivante[i][1],ecart,ecart)
    if key == 'ENTER':
        lancement = not lancement
        sleep(0.1)

run()