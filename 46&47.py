class library :
    def __init__ (self , book ,shelf):
        self.book = book
        self.shelf= shelf
    def printt(self):
        print(self.book, self.shelf)


object=library(300,45)
print(object.book)
print(object.shelf)

class science_section (library):
    def __init__(self, book,shelf, name):
        super(). __init__(book,shelf)
        self.name= name
    def print(self):
        print(self.book, self.shelf ,self.name)
ob =science_section(20,4,"physics books")
print(ob.book)
print(ob.shelf)
print(ob.name)
    
        
