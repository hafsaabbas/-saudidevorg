import re
str = "The rain in Spain"
x = re.sub("\s","9",str)
print(x)

import re
str = "The rain in Spain"
x = re.sub("ai",str)
print(x)

import re
str = "The rain in Spain"
x = re.sub(r"\bs\w+",str)
print(x.span())

import re
str = "The rain in Spain"
x = re.sub(r"\bs\w+",str)
print(x.string)

import re
str = "The rain in Spain"
x = re.sub(r"\bs\w+",str)
print(x.group())
