# écire une fonction listeN(n) qui reçoit en argument un entier n, supposé positif ou nul,
# et qui renvoie la liste des entiers 1, 2, ..., n, dans cet ordre. Si n = 0, la liste renvoyée est vide.

import lib_liste_chainees
# réponse :
def listeN(n):
	lst = None
	for x in range(n, 0, -1):
		lst = lib_liste_chainees.Cellule(x, lst)
	return lst

# solution du manuel :
def corection_listeN(n):
	lst = None
	while n > 0:
		lst = lib_liste_chainees.Cellule(n, lst)
		n -= 1
	return lst
