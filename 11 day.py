Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=5
>>> print(x>3 or x <4 )
True
>>> y=5
>>> z=x
>>> print (x is not z)
False
>>> 
>>> print(x is not y)
False
>>> print(x!+ y)
SyntaxError: invalid syntax
>>> x["ap","ba"]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    x["ap","ba"]
TypeError: 'int' object is not subscriptable
>>> x=["ap","ba"]
>>> print ("ba" in x)
True
>>> 
