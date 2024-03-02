class Patern:
    def __init__(self,nom,ecart):
        """donne si nested, sa largeur, hauteur, a code pour l'afficher, sous la forme d'une liste"""
        self.nom = nom + ".rle"   #nom str du fichier ou ce citue le patern
        self.ecart = ecart
        #any(isinstance(i, list) for i in a)

    def multProche(self,val):
        return (val//self.ecart) * self.ecart


    def extractPattern(self):
        f = open(self.nom,"r")
        s = ''
        while True:
            l = f.readline()
            if l == '':             # Empty indicates end of file. An empty line would be '\n'
                break
            if l[0] =='#':
                continue
            if l[0] =='x':
                continue
            s = s + l[:-1]   # To remove EOL
        f.close()
        self.textPatern = s

    def transformPatern(self):
        lst = []
        currentFloor = []
        nbr = 1
        for a in self.textPatern:
            if a == "$":
                lst.append(currentFloor)
                currentFloor = []
            elif a == 'b':
                currentFloor += [0 for _ in range(nbr)]
                nbr=1
            elif a == 'o':
                currentFloor += [1 for _ in range(nbr)]
                nbr=1
            else:
                if nbr != 1:
                    nbr = int(str(nbr)+a)
                else:
                    nbr = int(a)
        lst.append(currentFloor)
        self.listPatern = lst
        

    def addPatern(self,posX,posY,lst):
        for j in range(len(self.listPatern)):
            for i,cell in enumerate(self.listPatern[j]):
                if cell == 1:
                    lst.append((self.multProche((posX + i * self.ecart)),self.multProche((posY + j * self.ecart))))