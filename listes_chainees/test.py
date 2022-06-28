import lib_liste_chainees
import unittest
import ex48p124
import ex50p124
import ex54p125
import ex58p125
import ex55p125

class TestEx(unittest.TestCase):
    def test_ex48p124(self):
        valeur_a_tester = [0, 4]
        for element in valeur_a_tester:
            solution = ex48p124.corection_listeN(element)
            reponse = ex48p124.listeN(element)
            lstc = []
            lsts = []
            while solution and reponse is not None:
                lstc.append(solution.valeur)
                lsts.append(reponse.valeur)
                solution = solution.suivante
                reponse = reponse.suivante
            self.assertEqual(lstc, lsts)

    def test_ex50p124(self):
        lst = lib_liste_chainees.Cellule(1, lib_liste_chainees.Cellule(2, lib_liste_chainees.Cellule(3, lib_liste_chainees.Cellule(4, lib_liste_chainees.Cellule(5, lib_liste_chainees.Cellule(6, None))))))
        n = [0, 1, 5]
        for element in n:
            solution = ex50p124.corection_nieme_element(element, lst)
            reponse = ex50p124.corection_nieme_element(element, lst)
            self.assertEqual(solution, reponse)

    def test_ex54p125(self):
        l1 = lib_liste_chainees.Cellule(1, lib_liste_chainees.Cellule(2, lib_liste_chainees.Cellule(3, lib_liste_chainees.Cellule(4,lib_liste_chainees.Cellule(5,lib_liste_chainees.Cellule(6, None))))))
        l2 = lib_liste_chainees.Cellule(1, lib_liste_chainees.Cellule(2, lib_liste_chainees.Cellule(3, lib_liste_chainees.Cellule(4,lib_liste_chainees.Cellule(5,lib_liste_chainees.Cellule(6, None))))))
        if ex54p125.identiques(l1, l2) == True:
            l1 = lib_liste_chainees.Cellule(4, lib_liste_chainees.Cellule(2, lib_liste_chainees.Cellule(3, None)))
            l2 = lib_liste_chainees.Cellule(2, lib_liste_chainees.Cellule(3, lib_liste_chainees.Cellule(4,lib_liste_chainees.Cellule(5,lib_liste_chainees.Cellule(6, None)))))
            if ex54p125.identiques(l1, l2) == False:
                l1 = lib_liste_chainees.Cellule(4, lib_liste_chainees.Cellule(2, lib_liste_chainees.Cellule(3, None)))
                l2 = lib_liste_chainees.Cellule(2, lib_liste_chainees.Cellule(2, lib_liste_chainees.Cellule(3, None)))
                if ex54p125.identiques(l1, l2) == False:
                    self.assertEqual(1, 1)

    def test_ex58p125(self):
        test_ok = 0
        lst = lib_liste_chainees.Cellule(1, lib_liste_chainees.Cellule(2, lib_liste_chainees.Cellule(3, None)))
        if ex58p125.derniere_cellule(lst) == 3:
            test_ok += 1
        lst = lib_liste_chainees.Cellule(2, lib_liste_chainees.Cellule('chat', None))
        if ex58p125.derniere_cellule(lst) == 'chat':
            test_ok += 1
        lst = lib_liste_chainees.Cellule(2, None)
        if ex58p125.derniere_cellule(lst) == 2:
            test_ok += 1
        self.assertEqual(test_ok, 3)

    def test_ex55p125(self):
        test_ok = 0
        x = 3
        lst = lib_liste_chainees.Cellule(1, lib_liste_chainees.Cellule(2, lib_liste_chainees.Cellule(7, lib_liste_chainees.Cellule(9, None))))
        if ex54p125.identiques(ex55p125.inserer(x, lst), lib_liste_chainees.Cellule(1, lib_liste_chainees.Cellule(2, lib_liste_chainees.Cellule(3, lib_liste_chainees.Cellule(7, lib_liste_chainees.Cellule(9, None)))))):
            test_ok += 1
        lst = lib_liste_chainees.Cellule(4, lib_liste_chainees.Cellule(7, None))

        if ex54p125.identiques(ex55p125.inserer(x, lst), lib_liste_chainees.Cellule(3, lib_liste_chainees.Cellule(4, lib_liste_chainees.Cellule(7, None)))):
            test_ok += 1

        lst = lib_liste_chainees.Cellule(2, None)
        if ex54p125.identiques(ex55p125.inserer(x, lst), lib_liste_chainees.Cellule(2, lib_liste_chainees.Cellule(3, None))):
            test_ok += 1
        self.assertEqual(test_ok, 3)


if __name__ == '__main__':
    unittest.main()
