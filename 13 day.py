Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s =[]
>>> print(s)
[]
>>> n=[1,2,3,4,5]
>>> print(n)
[1, 2, 3, 4, 5]
>>> t=["apple","orange","banana",1,2]
>>> print(t)
['apple', 'orange', 'banana', 1, 2]
>>> c=[1.00,1.33,3.54]
>>> print(c)
[1.0, 1.33, 3.54]
>>> print(t[1])
orange
>>> for x in t:
	print(x)

	
apple
orange
banana
1
2
>>> > for z in c:
	print(z)
	
SyntaxError: invalid syntax
>>> for z in c:
	print(z)

	
1.0
1.33
3.54
>>> t[1]="limon"
>>> print(t)
['apple', 'limon', 'banana', 1, 2]
>>> del t[0]
>>> print(t)
['limon', 'banana', 1, 2]
>>> del t
>>> print(t)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print(t)
NameError: name 't' is not defined
>>> 
