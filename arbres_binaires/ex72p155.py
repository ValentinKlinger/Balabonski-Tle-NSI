# ecrire une fonction affiche(a) qui imprime un arbre sous la forme suivante :
# pour un arbre vide, on n'imprime rien; 
# pour un nœud, on imprime une parenthèse ouvrante, 
# son sous-arbre gauche (récursivement), sa valeur, 
# son sous-arbre droit (récusivement),puis enfin une parenthèse fermante.
from class_abres_binaires import Noeud, taille, hauteur, parcours_infixe

def affiche(a):
    if a is None:
        return 

    print('(', end='')
    affiche(a.gauche)
    print(a.valeur, end="")
    affiche(a.droit)
    print(")", end="")
