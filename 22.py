Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> dic={}
>>> print(dic)
{}
>>> dic={"brand":"ford"}
>>> print (dic)
{'brand': 'ford'}
>>> dic={"brand":"ford" , "model":"mustang", "year":1928}
>>> x=dic["model"]
>>> print(x)
mustang
>>> x=dic.get("model")
>>> print(x)
mustang
>>> dic["year"] =1234
>>> print(dic)
{'brand': 'ford', 'model': 'mustang', 'year': 1234}
>>> for t in dic:
	print(t)

	
brand
model
year
>>>  for t in dic:
	print(dic[t])
	
SyntaxError: unexpected indent
>>> for t in dic:
	print(dic[t])

	
ford
mustang
1234
>>>  print(dic.value())
 
SyntaxError: unexpected indent
>>> 
>>> print(dic.value())
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    print(dic.value())
AttributeError: 'dict' object has no attribute 'value'

>>> print(dic.values())
dict_values(['ford', 'mustang', 1234])
>>> print(dic.items())
dict_items([('brand', 'ford'), ('model', 'mustang'), ('year', 1234)])
>>> 
