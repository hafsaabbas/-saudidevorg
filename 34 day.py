def myfun(food):
    for x in food :
        print (x)

fr=["apple","banan","limon"]
myfun(fr)

def myfun1(x):
    return 5*x
print(myfun1(3))

def my(ch3,ch2,ch1):
    print("child"+ch3)
my(ch1="e",ch2="t",ch3="l")

def g(k):
    if(k>0):
        r=k+g(k-1)
        print(r)
    else:
         r=0
    return r
print("r ex e")
g(6)
