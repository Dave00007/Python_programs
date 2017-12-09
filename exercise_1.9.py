'''
Napisz skrypt usuwajacy z wejsciowego ciagu tekstowego (wybierz kilka plików z repozytorium: Tekstowego) nastepujace slowa : sie, i, oraz, nigdy, dlaczego.
'''
import os


def removeFromFileWords(path):
    wordsToRemove = ['się', 'i', 'oraz', 'nigdy', 'dlaczego']

    with open(path) as file:
        words = file.read().split()
        print(words)
        newWords = ''
        for word in words:
            if word in wordsToRemove:
                words.remove(word)
            else:
                newWords = newWords + ' ' + word
        print(words)
        print(newWords)
        file.close()

    with open(path, "w") as file:
        file.write(newWords)
        file.close()


path = os.getcwd()  # path to the current directory contains scripts
nameOfFile = 'text.txt'
path = os.path.join(path, nameOfFile)

removeFromFileWords(path)
