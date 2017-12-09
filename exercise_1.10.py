'''
Napisz skrypt zmieniajacy w podanym ciagu wejsciowym (wybierz kilka plików z repozytorium: Tekstowego) nastepujace slowa : i, oraz, nigdy,
dlaczego na nastepujacy zestaw slów : oraz, i, prawie nigdy, czemu. Zalecana struktura jest slownik
'''
import os


def replaceWords(path):
    wordsToReplace = ['i', 'oraz', 'nigdy', 'dlaczego']
    synonyms = ['oraz', 'i', 'prawie nigdy', 'czemu']

    with open(path) as file:
        words = file.read().split()
        newWords = ''

        for word in words:

            if word in wordsToReplace:
                index = words.index(word)
                index_1 = wordsToReplace.index(word)
                words[index] = synonyms[index_1]
                word = synonyms[index_1]
            newWords = newWords + ' ' + word

        print(words)
        print(newWords)
        file.close()

    with open(path, "w") as file:
        file.write(newWords)
        file.close()


path = os.getcwd()  # path to the current directory contains scripts
nameOfFile = 'text_1.txt'
path = os.path.join(path, nameOfFile)

replaceWords(path)