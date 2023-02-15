# Ecrire une fonction parfait(h) qui reçoit en argument un entier h supérieur ou égal
# à zéro et renvoie un arbre binaire parfait de hauteur h.
from class_abres_binaires import *

def parfait(h):
    if h == 0:
        return None 
    return Noeud(parfait(h-1), h, parfait(h-1))