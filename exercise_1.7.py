'''
Napisz skrypt obliczajacy pierwiastki równania kwadratowego w postaci : y = ax^2 + bx + c. Wejsciem skryptu sa wartosci: a, b, c
'''
import math


def solveQuadraticEquation(a, b, c):
    d = b ** 2 - (4 * a * c)

    if d < 0:
        print("Lack of solution")

    elif d == 0:
        x1 = -1*b/(2*a)
        print("Solution: " + str(x1))

    else:
        x1 = (-1*b - math.sqrt(d))/(2*a)
        x2 = (-1*b + math.sqrt(d))/(2*a)
        print("Solution: " + str(x1) + ", " + str(x2))


a = int(input("Enter first factor of quadratic equation: "))
b = int(input("Enter second factor of quadratic equation: "))
c = int(input("Enter third factor of quadratic equation: "))
solveQuadraticEquation(a, b, c)
