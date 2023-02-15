class Noeud:
    
    def __init__(self, g, v,d):
        self.gauche = g
        self.valeur = v
        self.droit = d

def taille(a):
    if a is None:
        return 0
    else:
        return 1 + taille(a.gauche) + taille(a.droit)

def hauteur(a):
    if a is None:
        return 0
    else:
        return 1 + max(hauteur(a.gauche), hauteur(a.droit))

def parcours_infixe(a):
    if a is None:
        return 
    parcours_infixe(a.gauche)
    print(a.valeur)
    parcours_infixe(a.droit)
