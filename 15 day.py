Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> y=["apple","banana","cherry"]
>>> print(len(y))
3
>>> y.append("orange")
>>> print(y)
['apple', 'banana', 'cherry', 'orange']
>>> y.insert(1,"orange")
>>> print(y)
['apple', 'orange', 'banana', 'cherry', 'orange']
>>> y.remove("banana")
>>> print(y)
['apple', 'orange', 'cherry', 'orange']
>>> y.pop()
'orange'
>>> print(y)
['apple', 'orange', 'cherry']
>>> y.clear()
>>> print(y)
[]
>>> m=y.copy()
>>> print(m)
[]
>>> y=["apple","banana","cherry"]
>>> m=list(y)
>>> print(m)
['apple', 'banana', 'cherry']
>>> m=list(("apple","orange","banana"))
>>> print(m)
['apple', 'orange', 'banana']
>>> 
