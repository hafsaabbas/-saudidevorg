Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> dic={"brand":"ford" ,"model":"mustang","year":1964}
>>> mydic=dic.copy()
>>> print(mydic)
{'brand': 'ford', 'model': 'mustang', 'year': 1964}
>>> mydic=dict(dic)
>>> print(mydic)
{'brand': 'ford', 'model': 'mustang', 'year': 1964}
>>> myfamily={"ch1":{"name":"email"},"ch2":{"name":"fa","year":123},"ch3":{"name":"Ds","year":23}}
>>> print(myfamily)
{'ch1': {'name': 'email'}, 'ch2': {'name': 'fa', 'year': 123}, 'ch3': {'name': 'Ds', 'year': 23}}
>>> ch1 ={"name":"email"}
>>> ch2={"name":"fa","year":123}
>>> ch3={"name":"Ds","year":23}
>>>  myfamily={"ch1":ch1,"ch2":ch2,"ch3":ch3}
 
SyntaxError: unexpected indent
>>> myfamily={"ch1":ch1,"ch2":ch2,"ch3":ch3}
>>> 
KeyboardInterrupt
>>> print(myfamily)
{'ch1': {'name': 'email'}, 'ch2': {'name': 'fa', 'year': 123}, 'ch3': {'name': 'Ds', 'year': 23}}
>>> dic=dict(brand="ford" ,model="mustang",year=1964)
>>> print(dic)
{'brand': 'ford', 'model': 'mustang', 'year': 1964}
>>> 
