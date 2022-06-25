# écrire une fonction identiques(l1, l2 qui renvoie un booléen indiquant si les listes l1 et l2 sont identiques, c'est-à-dire contiennent exactement les mêmes éléments, dans le même ordre. On supose que l'on peut comparer les éléménents de l1 et l2 avec l'égalité == de python.
import config

# ma réponse
def identiques(l1, l2):
	if l1 is None:
		return l2 is None
	if l2 is None:
		return l1 is None
	return l1.valeur == l2.valeur and identiques(l1.suivante, l2.suivante)

# solution du manuel
def corection_identiques(l1, l2):
	if l1 is None:
		return l2 is None
	if l2 is None:
		return l1 is None
	return l1.valeur == l2.valeur and correction_identiques(l1.suivante, l2.suivante)
