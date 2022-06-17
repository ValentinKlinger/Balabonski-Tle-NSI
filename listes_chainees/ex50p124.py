# réécrire la fonction nieme_element (programme 20 page 114) avec une boucle while.

# réponse :
def nieme_element(n, lst):
	c = lst
	while c is not None and n != 0:
		n = n - 1
		c = lst.suivante
	
	if c is None:
		raise IndexError("indice invalide")
	if n == 0:
		return c.valeur

# solution du manuel :
def nieme_element(n, lst):
	i = 0
	c = lst
	while i < n and c is not None:
		i += 1
		c = c.suivante
	if n < 0 or c is None:
		raise IndexError("indice invalide")
	return c.valeur
