'''
Napisz skrypt obliczajacy wartosc iloczynu dwóch wektorów : a = [1, 2, 12, 4], b = [2, 4, 2, 8], tzw. iloczyn skalarny wektorów.
'''


def scalarProduct(a, b):
    product = 0
    for i in range(len(a)):
        product = product + (a[i] * b[i])
    return product


a = [1, 2, 12, 4]
b = [2, 4, 2, 8]

score = scalarProduct(a, b)
print(score)
