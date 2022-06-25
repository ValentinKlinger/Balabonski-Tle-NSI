class Cellule:
	def __init__(self, v, s):
		self.valeur = v
		self.suivante = s

class Liste:
	def __init__(self):
		self.tete = None

	def est_vide(self):
		return self.tete is None

	def ajoute(self, x):
		self.tete = Cellule(x, self.tete)

	def __len__(self):
		return longueur(self.tete)

	def __getitem__(self, n):
		return nieme_element(n, self.tete)

	def reverse(self):
		self.tete = renverser(self.tete)

	def __add__(self, lst):
		r = Liste()
		r.tete = concatener(self.tete, test.tete)
		return r

	def reverse(self):
		self.tete = renverser(self.tete)

def longeur(lst):
	if lst is None:
		return 0
	else:
		return 1 + longueur(lst.suivante)

def concactener(l1, l2):
	if l1 is None:
		return l2
	else:
		return Cellule(l1.valeur, concatener(l1.suivante, l2))

def nieme_element(n, lst):
	if lst is None:
		raise IndexError("indice invalide")
	if n == 0:
		return lst.valeur
	else:
		return nieme_element(n - 1, lst.suivante)

def renverser(lst):
	r = None
	c = lst
	while c is not None:
		r = Cellule(c.valeur, r)
		c = c.suivante
	return r

def convertir(lst):
	c = lst
	list = []
	while c is not None:
		list.append(c.valeur)
		c = c.suivante
	return list


#def cree_cellule(liste_python):
#	for element in range(liste_python):
