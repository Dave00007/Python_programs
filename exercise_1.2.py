'''
Napisz skrypt, który pyta o imie, nazwisko i rok urodzenia (powinny byc podane w jednej linii)
'''

name, surname, dateOfBirth = input("Enter your name, surname, date of birth in one line: ").split()
print('Your name: ' + name + ', surname: ' + surname + ', date of birth: ' + dateOfBirth)
