# écrire une fonction inserer(x, lst) qui prend en arguments un entier x et une liste lst,
#supposée triée par ordre croissant, et qui renvoie une nouvelle liste dans la quel x a été inséré à sa place.
# Ainsi, insérer la valeur 3 dans la liste 1, 2, 5, 8 renvoie la liste 1, 2, 3, 5, 8.
# On suggère de l'écrire comme une fonction récursive.
import config

# réponse
def inserer(x, lst):
    r = None
    c = lst
    while c is not None:
        if x is not None and (c.suivante is None or c.valeur >= x):
            if c.valeur < x:
                r = config.Cellule(c.valeur, r)
                r = config.Cellule(x, r)
            else:
                r = config.Cellule(x, r)
                r = config.Cellule(c.valeur, r)
            c = c.suivante
            x = None
        else:
            r = config.Cellule(c.valeur, r)
            c = c.suivante
    return config.renverser(r)

def solution_inserer(x, lst):
    if lst is None or x <= lst.valeur:
        return config.Cellule(lst.valeur, solution_inserer(x. lst.suivante))
