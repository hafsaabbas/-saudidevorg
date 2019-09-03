Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> y=()
>>> print(y)
()
>>> y=(3,)
>>> print(y)
(3,)
>>> y=
SyntaxError: invalid syntax
>>> y=("app;e",1,1.2,"CF")
>>> print(y)
('app;e', 1, 1.2, 'CF')
>>> print(y(1))
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print(y(1))
TypeError: 'tuple' object is not callable
>>> print(y[1])
1
>>> for x in y
SyntaxError: invalid syntax
>>> for x in y:
	print(x)

	
app;e
1
1.2
CF
>>> y[4]="df"
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    y[4]="df"
TypeError: 'tuple' object does not support item assignment
>>> del y
>>> print(y)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print(y)
NameError: name 'y' is not defined
>>> print(y[0:2])
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print(y[0:2])
NameError: name 'y' is not defined
>>> 
