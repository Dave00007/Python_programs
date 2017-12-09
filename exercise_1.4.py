'''
Napisz skrypt realizujacy funkcji zamka szyfrowego. Prosi o podanie kodu i nastepnie sprawdza czy jest on zgodny z wczesniej wprowadzonym kodem.
'''

codeOfLock = input("Enter code for the lock: ")

if codeOfLock == '1234':
    print('Congratulations! The code is correct!')
else:
    print('The code is incorrect.')