Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> age =60
>>> txt = "hafsa , and age {}"
>>> print(txt.format(age))
hafsa , and age 60
>>> q=3
>>> i=234
>>> p=34.3
>>> m="i want {} prices of item {} for{} dollars"
>>> print(m.format(q,i,p))
i want 3 prices of item 234 for34.3 dollars
>>> m="i want {2} prices of item {1} for{0} dollars"
>>> print(m.format(q,i,p))
i want 34.3 prices of item 234 for3 dollars
>>> 
