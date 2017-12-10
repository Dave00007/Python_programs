'''
Operacje wejscia/wyjscia (zapisac i odczytac dane)
'''

nameOfFile = 'exampleFile.txt'
file = open(nameOfFile, 'w')
file.write("Everything works")
file.close()

file = open(nameOfFile)
data = file.read()
file.close()

print(data)