Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> set={1,3,5,7,8}
>>> print(set)
{1, 3, 5, 7, 8}
>>> set.add(4,8,12)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    set.add(4,8,12)
TypeError: add() takes exactly one argument (3 given)
>>> set.add("4","8","!2")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    set.add("4","8","!2")
TypeError: add() takes exactly one argument (3 given)
>>> set.add(4)
>>> set.add(8)
>>> set.add(12)
>>> print(set)
{1, 3, 4, 5, 7, 8, 12}
>>> set.remove(8)
>>> print(set)
{1, 3, 4, 5, 7, 12}
>>> set.clear()
>>> print(set)
set()
>>> dic={"name":"pigon","type":"bride","skin cover":"feathers"}
>>> x=dic["type"]
>>> print(x)
bride
>>> dic["skin cover"] ="black"
>>> print(dic)
{'name': 'pigon', 'type': 'bride', 'skin cover': 'black'}
>>> 
