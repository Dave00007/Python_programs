'''
Napisz skrypt realizujacy mnozenie dwóch macierzy o rozmiarach 8x8
'''
import random


def generateMatrix(matrixSize):
    matrix = [[random.randint(0,9)for i in range(matrixSize)] for j in range(matrixSize)]
    return matrix

def multiplicationMatrices(matrix1,matrix2):
    sizeOfMatrix = len(matrix1)
    matrix = [[0 for i in range(sizeOfMatrix)] for j in range(sizeOfMatrix)]

    for i in range(sizeOfMatrix):
        for j in range(sizeOfMatrix):
            for k in range(sizeOfMatrix):
                matrix[i][j] = matrix[i][j] + (matrix1[j][k]) * (matrix2[k][j])

    return matrix


matrix1 = generateMatrix(8)
matrix2 = generateMatrix(8)
matrix = multiplicationMatrices(matrix1, matrix2)

print(matrix1)
print(matrix2)
print(matrix)
