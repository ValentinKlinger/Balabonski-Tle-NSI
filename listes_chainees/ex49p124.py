# écrire une fonction affiche_liste(lst) qui affiche en utilisant la fonction print, tous les éléments
# de la liste chainée lst, séparés par des espaces, suivi d'un retour chariot.
# l'écrire avec une fonction récursive et une boucle while
import lib_liste_chainees

def affiche_liste_recursive(lst):
    c = lst
    if c is None:
        pass
    else:
        print(c.valeur, end=" ")
        affiche_liste_recursive(c.suivante)

def affiche_liste_loop(lst):
    c = lst
    while c is not None:
        print(c.valeur, end=" ")
        c = c.suivante
