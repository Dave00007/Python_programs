'''
Napisz rekurencyjne przejscie drzewa katalogów i wypisanie plików, które znajduja sie w eksplorowanej strukturze
'''
import os


def displayContentsOfFolder(path):
    listOfFiles = os.listdir(path)

    for i in listOfFiles:
        internalPath = os.path.join(path, i)

        if os.path.isdir(internalPath):
            displayContentsOfFolder(internalPath)
        else:
            print(internalPath)


path = os.getcwd()  # path to the current directory contains scripts
displayContentsOfFolder(path)