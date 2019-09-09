Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> sets={"banana","orange","apple"}
>>> print(len(sets))
3
>>> sets.remove("banana")
>>> print(sets)
{'orange', 'apple'}
>>> sets.discard("orange")
>>> print(sets)
{'apple'}
>>> sets={"banana","orange","apple"}
>>> x=sets.pop()
>>> print(x)
orange
>>> print(sets)
{'apple', 'banana'}
>>> sets.clear()
>>> print(sets)
set()
>>> del sets
>>> print(sets)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print(sets)
NameError: name 'sets' is not defined
>>> r=set(("sa","As","asd"))
>>> print(r)
{'asd', 'sa', 'As'}
>>> 
