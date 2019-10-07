class person :
    def __init__(self,fname,lname):
        self.fristname=fname
        self.lastname=lname
    def printname(self):
        print(self.fristname, self.lastname)

x = person ( "johan" ," Doe")
x.printname()
    
    
    
class person :
    def __init__(self,fname,lname):
        self.fristname=fname
        self.lastname=lname
    def printname(self):
        print(self.fristname, self.lastname)
class student(person):
    pass

x = student ( "mike" ," Doe")
x.printname()

    
class person :
    def __init__(self,fname,lname):
        self.fristname=fname
        self.lastname=lname
    def printname(self):
        print(self.fristname, self.lastname)
class student(person):
    def __init__(self,fname,lname):
        person.__init__(self,fname,lname)

x = student ( "mike" ," Doe")
x.printname()
