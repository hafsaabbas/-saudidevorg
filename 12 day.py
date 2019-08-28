Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> t="please, I Want {} sandwish and {} donuts"
>>> print(t.replace("i","we"))
please, I Want {} sandwwesh and {} donuts
>>> x=5
>>> y=7
>>> print(t.format(x,y))
please, I Want 5 sandwish and 7 donuts
>>> print(t.upper(a))
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(t.upper(a))
NameError: name 'a' is not defined
>>> print(t.upper())
PLEASE, I WANT {} SANDWISH AND {} DONUTS
>>> 
