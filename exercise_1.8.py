'''
Napisz skrypt sortujacy liczby malejaco. Wygeneruj losowo 50 liczb - wykorzystaj standardowa funkcje do losowania. Z wbudowanej funkcji
sortujacej korzystaj tylko w celu weryfkacji wyników
'''
from random import seed, random


def createRandomNumbers(amount):
    seed()
    numbers = []
    for i in range(amount):
        numbers.append(random())
    return numbers


def swap(t1, t2):
    return t2, t1


def sortingDescending(randomNumbers):
    for j in range(N - 1):
        for i in range(N - 1):
            if randomNumbers[i] < randomNumbers[i + 1]:
                randomNumbers[i], randomNumbers[i + 1] = swap(randomNumbers[i], randomNumbers[i + 1])
    return randomNumbers


N = 50
randomNumbers = createRandomNumbers(N)
print(randomNumbers)
print(sorted(randomNumbers, reverse=True))

sortedNumbers = sortingDescending(randomNumbers)
print(sortedNumbers)

