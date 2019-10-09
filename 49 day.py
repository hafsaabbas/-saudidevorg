
x=300

def fun ():
    x=200
    print(X)
fun()
print(X)


def mfun ():

    global x
    x=300
   
mfun()
print(X)

x=300

def fun ():
    global x
    x=200
fun()
print(X)
