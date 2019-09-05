Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> t=("apple","banan","orange")
>>> if "apple" in t:
	print("yes, 'apple' is in the fruits")

	
yes, 'apple' is in the fruits
>>> x=("python")*3
>>> print(x)
pythonpythonpython
>>> x=("python")*3
>>> p= ("python",)*3
>>> print (p)
('python', 'python', 'python')
>>> c=p+t
>>> ptint(c)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    ptint(c)
NameError: name 'ptint' is not defined
>>> p=("qdd","hafsj")
>>> print(c)
('python', 'python', 'python', 'apple', 'banan', 'orange')
>>> x=(1,2,3)
>>> x=x+(1,2,3)
>>> print(x)
(1, 2, 3, 1, 2, 3)
>>> print(len(x))
6
>>> v=tuple(("gh","cf","gg"))
>>> print(v)
('gh', 'cf', 'gg')
>>> f=[1,2,4,5,6]
>>> a=tuple(f)
>>> print(a)
(1, 2, 4, 5, 6)
>>> 
