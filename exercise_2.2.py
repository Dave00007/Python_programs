'''
Zdefniowac klase reprezentujaca liczby zespolone (wraz z funkcjami na
nich dzialajacymi np. modul, dodawanie, odejmowanie itd.)
'''
import cmath


class ComplexNumbers:

    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __add__(self, other):
        newRe = self.re + other.re
        newIm = self.im + other.im
        return ComplexNumbers(newRe, newIm)

    def __sub__(self, other):
        newRe = self.re - other.re
        newIm = self.im - other.im
        return ComplexNumbers(newRe, newIm)

    def __mul__(self, other):
        newRe = self.re * other.re - self.im * other.im
        newIm = self.im * other.re + self.re + other.im
        return ComplexNumbers(newRe, newIm)

    def __truediv__(self, other):
        try:
            newRe = (self.re * other.re + self.im * other.im)/(other.re**2+other.im**2)
            newIm = (self.im * other.re - self.re + other.im)/(other.re**2+other.im**2)
            return ComplexNumbers(newRe, newIm)
        except ZeroDivisionError:
            print("Exception!")

    def module(self):
        return (self.re**2 + self.im**2) ** (1/2)

    def angle(self):
        if self.re > 0:
            angle = cmath.atan(self.im / self.re)
        elif self.re < 0:
            angle = cmath.atan(self.im / self.re) + cmath.pi
        elif self.re == 0 and self.im > 0:
            angle = 0.5 * cmath.pi
        elif self.re == 0 and self.im < 0:
            angle = -0.5 * cmath.pi
        elif self.re == 0 and self.im == 0:
            angle = 0
        return angle

    def display(self):
        sign = ''
        if self.im >= 0:
            sign = '+'
        print(str(self.re) + sign + str(self.im) + 'j')


number1 = ComplexNumbers(1, 3)
number2 = ComplexNumbers(2, 5)

print('Number 1:')
number1.display()
print('Number 2:')
number2.display()
print('+')
(number1 + number2).display()
print('-')
(number1 - number2).display()
print('*')
(number1 * number2).display()
print('/')
(number1 / number2).display()
print('||')
print(number1.module())
print('angle')
print(number1.angle())

