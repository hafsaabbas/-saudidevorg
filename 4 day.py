Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=1 #int
>>> y=2.8 #float
>>> z=1j #complex
>>> print(type(x))
<class 'int'>
>>> 
>>> print(type(y))
<class 'float'>
>>> print(type(z))
<class 'complex'>
>>> a=float(x)
>>> b=int(y)
>>> c=complex(x)
>>> print(a)
1.0
>>> print(b)
2
>>> print(c)
(1+0j)
>>> print(type(a))
<class 'float'>
>>> print(type(b))
<class 'int'>
>>> print(type(c))
<class 'complex'>
>>> x random
SyntaxError: invalid syntax
>>> import random
>>> print(random.randrange(1,10))
3
>>> 
>>> print(random.randrange(1,10))
8
>>> print(random.randrange(1,10))
3
>>> 
