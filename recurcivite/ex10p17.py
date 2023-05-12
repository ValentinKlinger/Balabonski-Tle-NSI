# Courbe de Koch

import turtle

def koch(n, l):
    if n == 0:
        turtle.fd(l)
    else:
        koch(n - 1, l/3)
        turtle.left(60)
        koch(n - 1, l/3)
        turtle.right(120)
        koch(n - 1, l/3)
        turtle.left(60)
        koch(n - 1, l/3)

if __name__ == '__main__':
    turtle.up()
    turtle.setx(-350)
    turtle.down()
    koch(3, 600) 
