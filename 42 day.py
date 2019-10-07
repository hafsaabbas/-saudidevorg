class person:
    def __init__ (self,name,age):
        self.name = name
        self.age = age
    def myfun (self) :
        print("hello"+ self.name)

p1= person("johan",36)
p1.myfun()

class person:
    def __init__ (self,name,age):
        self.name = name
        self.age = age
    def myfun (self) :
        print("hello"+ self.name)

p1= person("johan",36)
p1.age =40
print(p1.age)


class person:
    def __init__ (self,name,age):
        self.name = name
        self.age = age
    def myfun (self) :
        print("hello"+ self.name)

p1= person("johan",36)
del p1.age 
print(p1.age)
class person:
    def __init__ (self,name,age):
        self.name = name
        self.age = age
    def myfun (self) :
        print("hello"+ self.name)

p1= person("johan",36)
del p1
print(p1)
