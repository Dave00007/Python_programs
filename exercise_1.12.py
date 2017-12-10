'''
Napisz skrypt sumujacy dwie macierze o rozmiarach 128x128. Wykorzystaj generator liczb losowych do wygenerowania macierzy.
'''
import random
import numpy


def generateMatrix(matrixSize):
    matrix = [[random.randint(0,9) for i in range(matrixSize)] for j in range(matrixSize)]
    return matrix


def addMatrices(matrix1,matrix2):
    if numpy.shape(matrix1) != numpy.shape(matrix2):
        print("Wrong size of matrices")
        return

    sizeOfMatrix = len(matrix1)
    matrix = [[0 for i in range(sizeOfMatrix)] for j in range(sizeOfMatrix)]
    for i in range(sizeOfMatrix):
        for j in range(sizeOfMatrix):
            matrix[i][j]= matrix1[i][j]+matrix2[i][j]
    return matrix


matrix1 = generateMatrix(128)
matrix2 = generateMatrix(128)
matrix = addMatrices(matrix1, matrix2)

print(matrix1)
print(matrix2)
print(matrix)