import re
str = "The rain in Spain"
x = re.findall ("ai",str)
print(x)

import re
str = "The rain in Spain"
x = re.findall ("peor",str)
print(x)

if(x):
    print("yes")
else:
    print("no")
    
import re
str = "The rain in Spain"
x = re.search("\s",str)
print("The :",x.start())

import re
str = "The rain in Spain"
x = re.split("\s",str)
print(x)
