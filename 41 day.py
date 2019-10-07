class Myclass:
    x=5
    print(Myclass)
    
class Myclass:
    x=5
p1= Myclass()
print(p1.x)



class person :
    def _init_(self,name,age):
        self.name=name
        self.age=age
 
p1=person("johan",23)
print(p1.name)
print(p1.age)


class person :
    def _init_(mysillyobject,name,age):
        mysillyobject.name=name
        mysillyobject.age=age

    def myfun(abc):
        print("hello"+abc.name)
p1=person("johan",23)
p1.myfun()
      
    
