'''
Sparsowac przygotowanego XML (parserem SAX i DOM) i go zmodyfikowac np. zmienic wartosc któregos tag'a.
'''
import xml.sax

# Script with SAX

class BookHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.author = ""
        self.title = ""
        self.genre = ""
        self.price = ""
        self.publish_date = ""
        self.description = ""

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "book":
            print("--Book--")
            id = attributes["id"]
            print("ID: " + id)

    def endElement(self, tag):
        if self.CurrentData == "author":
            print("Author: " + self.author)
        elif self.CurrentData == "title":
            print( "Title: " + self.title)
        elif self.CurrentData == "genre":
            print("Genre: " + self.genre)
        elif self.CurrentData == "price":\
            print("Price: " + self.price)
        elif self.CurrentData == "publish_date":\
            print("Publish_date: " + self.publish_date)
        elif self.CurrentData == "description":
            print("Description: " + self.description)
        self.CurrentData = ""

    def characters(self, content):
        if self.CurrentData == "author":
            self.author = content
        elif self.CurrentData == "title":
            self.title = content
        elif self.CurrentData == "genre":
            self.genre = content
        elif self.CurrentData == "price":
            self.price = content
        elif self.CurrentData == "publish_date":
            self.publish_date = content
        elif self.CurrentData == "description":
            self.description = content


parser = xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces, 0)
Handler = BookHandler()
parser.setContentHandler(Handler)
parser.parse("xmlFile.xml")
