'''
Napisz skrypt konwersji rozszerzen plików *.jpg na *.png (uprzednio stwórz zestaw 4 plików z rozszerzeniem *.jpg)
'''
from PIL import Image
import os


def saveAsPNG(path):
    pathJPG = path + '.jpg'
    pathPNG = path + '.png'

    image = Image.open(pathJPG)
    image.save(pathPNG)


path = os.getcwd()  # path to the current directory which contains scripts

nameOfImage = 'jowisz'
path = os.path.join(path, nameOfImage)
saveAsPNG(path)
