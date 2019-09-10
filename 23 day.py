Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> dic={"model":"ford","brand":"mus","year":12344}
>>> if "model" in dic:
	print("yyas")

	
yyas
>>> print(len(dic))
3
>>> 
>>> dic["black"]="color"
>>> print(dic)
{'model': 'ford', 'brand': 'mus', 'year': 12344, 'black': 'color'}
>>> dic.pop("model")
'ford'
>>> print(dic)
{'brand': 'mus', 'year': 12344, 'black': 'color'}
>>> dic.popitem()
('black', 'color')
>>> print(dic)
{'brand': 'mus', 'year': 12344}
>>> del dic["year"]
>>> print(dic)
{'brand': 'mus'}
>>> del dic
>>> print(dic)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print(dic)
NameError: name 'dic' is not defined
>>> dic={'model': 'ford', 'brand': 'mus', 'year':12344, 'black': 'color'}
>>> dic.clear()
>>> print(dic)
{}
>>> 
