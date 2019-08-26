Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=("hsafs,Abbas")
>>> print(a.strip())
hsafs,Abbas
>>> print(len(a))
11
>>> print(a.lower())
hsafs,abbas
>>> print(a.upper())
HSAFS,ABBAS
>>> print(a.replace("s","g"))
hgafg,Abbag
>>> print(a.spilt(","))
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print(a.spilt(","))
AttributeError: 'str' object has no attribute 'spilt'
>>> print(a.split(","))
['hsafs', 'Abbas']
>>> 
