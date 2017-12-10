'''
Sparsowac przygotowanego XML (parserem SAX i DOM) i go zmodyfikowac np. zmienic wartosc któregos tag'a.
'''
from xml.dom.minidom import parse
import xml.dom.minidom

# Script with DOM

DOMTree = xml.dom.minidom.parse("xmlFile.xml")
collection = DOMTree.documentElement

books = collection.getElementsByTagName("book")
for book in books:
    print("--Book--")
    if book.hasAttribute("id"):
        print("ID: " + book.getAttribute("id"))
        author = book.getElementsByTagName('author')[0]
        print("Type: " + author.childNodes[0].data)
        title = book.getElementsByTagName('title')[0]
        print("Title: " + title.childNodes[0].data)
        genre = book.getElementsByTagName('genre')[0]
        print("Genre: " + genre.childNodes[0].data)
        price = book.getElementsByTagName('price')[0]
        print("Price: " + price.childNodes[0].data)
        publish_date = book.getElementsByTagName('publish_date')[0]
        print("Publish_date: " + publish_date.childNodes[0].data)
        description = book.getElementsByTagName('description')[0]
        print("Description:  " + description.childNodes[0].data)


def replaceText(collection, node, valueOfNode, newText):
    books = collection.getElementsByTagName("book")
    for book in books:
        if book.hasAttribute("id"):

            if book.getElementsByTagName(node)[0].childNodes[0].data == valueOfNode:

                book.getElementsByTagName(node)[0].childNodes[0].replaceWholeText(newText)


replaceText(collection, 'genre', 'Horror', '--NEW HORROR--')
file_handle = open("xmlFileNEW.xml", "w")
collection.writexml(file_handle)
file_handle.close()