# écire une fonction listeN(n) qui reçoit en argument un entier n, supposé positif ou nul, et qui renvoie la liste des entiers 1, 2, ..., n, dans cet ordre. Si n = 0, la liste renvoyée est vide.

# réponse :
def listeN(n):
	l = [i + 1 for i in range(n)]
	lst = None 
	for x in l:
		lst = Cellule(l[-x], lst)
	return lst

# solution du manuel :
def listN(n):
	lst = None 
	while n > 0:
		lst = Cellule(n, lst)
		n -= 1
	return lst
