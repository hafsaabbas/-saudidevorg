class person :
    def __init__(self,fname,lname):
        self.firstname =fname
        self.lastname =lname
    def printname(self):
        print(self.firstname, self.lastname)
class student(person):
   def __init__(self,fname,lname):
       super().__init__(self,fname,lname)
x = student("mike","olsen")
x.printname()

class person :
    def __init__(self,fname,lname):
        self.firstname =fname
        self.lastname =lname
    def printname(self):
        print(self.firstname, self.lastname)
class student(person):
   def __init__(self,fname,lname):
       super().__init__(self,fname,lname)
       self.grand = 2019
x = student("mike","olsen")
print (x.grand)


class person :
    def __init__(self,fname,lname):
        self.firstname =fname
        self.lastname =lname
    def printname(self):
        print(self.firstname, self.lastname)
class student(person):
   def __init__(self,fname,lname,year):
       super().__init__(self,fname,lname)
       self.grand =year
x = student("mike","olsen",2019)
print (x.grand)


class person :
    def __init__(self,fname,lname):
        self.firstname =fname
        self.lastname =lname
    def printname(self):
        print(self.firstname, self.lastname)
class student(person):
   def __init__(self,fname,lname,year):
       super().__init__(self,fname,lname)
       self.grand =year
    def welcome (self):
        print("welcome", self.firstname , self.lastname , self.grand)
x = student("mike","olsen",2019)
x.welcome()
