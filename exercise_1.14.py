'''
Napisz skrypt wyliczajacy wyznacznik macierzy wygenerowanej losowo
'''
import random
import numpy

def determinantOfMatrix(matrix):
    if numpy.shape(matrix)[0] != numpy.shape(matrix)[1]:
        print("Wrong size of matrix.")
        return

    sizeOfMatrix = len(matrix)
    if sizeOfMatrix > 2:
        i = 1
        sum = 0
        for var1 in range(sizeOfMatrix):
            mat = {}
            for var2 in range(1, sizeOfMatrix):
                mat[var2] = []
                for var3 in range(sizeOfMatrix):
                    if var3 == var1:
                        u = 0
                    else:
                        mat[var2].append(matrix[var2][var3])
            matrix1 = [mat[x] for x in mat]
            sum = sum + i * (matrix[0][var1]) * (determinantOfMatrix(matrix1))
            i = i * (-1)
        return sum
    else:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def generateMatrix(matrixSize):
    matrix = [[random.randint(0, 9)for i in range(matrixSize)] for j in range(matrixSize)]
    return matrix


randomMatrix = generateMatrix(5)
det = determinantOfMatrix(randomMatrix)
print(det)