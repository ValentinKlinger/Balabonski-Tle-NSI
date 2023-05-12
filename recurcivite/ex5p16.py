# Ecrire une fonction récursive pgcd(a, b), qui renvoie PGCD de deux entiers a et b.

def pgcd(a, b):
    if a == 0:
        return b
    return pgcd(b % a, a)

if __name__ == '__main__':
    print(pgcd(6, 21))
