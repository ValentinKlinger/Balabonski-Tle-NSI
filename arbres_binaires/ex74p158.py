# Ajouter à la classe Neud une méthode __eq__ permétant de tester
# l'égalité entre deux arbres binaires avec l'opération ==.

class Noeud:
    
    def __init__(self, g, v,d):
        self.gauche = g
        self.valeur = v
        self.droit = d

    # début du programme

    def __eq__(self, autre_noeud):

        if self.valeur == autre_noeud.valeur:
            self.gauche.__eq__(autre_noeud.gauche)
            self.droit.__eq__(autre_noeud.droit)
            
        else:
            return False

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