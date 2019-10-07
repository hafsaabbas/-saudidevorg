tuple= ("apple","banana","cherry")
pe=iter(tuple)
print(next(pe))
print(next(pe))
print(next(pe))
t="banana"
ta=iter(t)
print(next(ta))
print(next(ta))
print(next(ta))
print(next(ta))
print(next(ta))
print(next(ta))
for x in tuple :
    print(x)
for y in t :
    print(y)

class num:
    def __iter__ (self):
        self.a= 1
        return self
    def __next__(self):
        f=self.a
        self.a +=1
        return f
myclass = num()
ite=iter(myclass)
print(next(ite))
print(next(ite))
print(next(ite))
print(next(ite))
print(next(ite))
class num1:
    def __iter__ (self):
        self.a= 1
        return self
    def __next__(self):
        if self.a <= 20:
            f=self.a
            self.a +=1
            return f
        else :
            raise StopIteration
                  
myclass1 =num1()
ite1=iter(myclass1)
for r in ite1 :
    print (r)
