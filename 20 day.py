Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> sets={"banana","orange","apple"}
>>> print(sets)
{'apple', 'orange', 'banana'}
>>> s={"bits",1,1,,3,"bits"}
SyntaxError: invalid syntax
>>> s={"bits",1,1,3,"bits"}
>>> print(s)
{1, 'bits', 3}
>>> for x in s:
	print(x)

	
1
bits
3
>>> 
>>> print ("bits" in s)
True
>>> sets.add("cherry")
>>> print(sets)
{'apple', 'orange', 'cherry', 'banana'}
>>> sets.update(["ve","cer"])
>>> print (sets)
{'cer', 'cherry', 'banana', 've', 'apple', 'orange'}
>>> 
