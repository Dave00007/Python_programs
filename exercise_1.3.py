'''
Napisz skrypt zliczajacy ilosc plików w katalogu /dev, skorzystaj ze standardowej biblioteki - os
'''
import os


def numberOfFiles(path):
    listOfFiles = os.listdir(path)
    numberOfFiles = len(listOfFiles)
    print("Number of files: " + str(numberOfFiles))


path = os.getcwd()  # path to the current directory which contains scripts
numberOfFiles(path)
