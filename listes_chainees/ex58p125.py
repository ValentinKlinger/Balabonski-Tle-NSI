# écrire une fonction derniere_cellule(lst) qui renvoie la dernière cellule de la liste lst.
# On supose la liste lst non vide
import config
# réponse
def derniere_cellule(lst):
    c = lst
    if c.suivante is not None:
        return derniere_cellule(c.suivante)
    else:
        return c.valeur

# solution manuel :
def corection_derniere_cellule(lst):
    c = lst
    while c.suivante is not None:
        c = c.suivante
    return c
