def fun(x):
    return x^3
print(fun(5))
    
z=[-4,-6,-5,-1,2,3,7,9,88]
print(z)
pos=[]
post=lambda n:n>0
for n in z:
    if(post(n)):
        pos.append(n)
        print(pos)
