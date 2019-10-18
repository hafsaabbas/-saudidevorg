import json

x = {"name": "john" , "age": 30 , "city" :"new york",
     "child":("asSD","Sdf"),
     "pets":None,
     "cars": [{"mo":"bmw","mpg":27.3},{"mo":"nvnv" ,"mod":34}]}
print(json.dumps(x,indenr=4))


import json

x = {"name": "john" , "age": 30 , "city" :"new york",
     "child":("asSD","Sdf"),
     "pets":None,
     "cars": [{"mo":"bmw","mpg":27.3},{"mo":"nvnv" ,"mod":34}]}
print(json.dumps(x,indenr=4, separators= (".","=")))
