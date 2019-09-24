def my1(n):
    return lambda a:a*n
myd=my1(2)
print(myd(11))

def my2(n):
    return lambda a:a*n
mydd=my2(3)
print(mydd(11))



def my2(n):
    return lambda a:a*n
mydd=my2(3)
myd=my1(2)
print(mydd(11))
print(myd(11))
