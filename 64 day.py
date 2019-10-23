try:
    print(x)
except:
    print("an exception occured")

print(x)

try:
    print(x)
except NameError:
    print("x not defend")
except:
    print("Somthing else went wrong")

try:
    print("hello")
except:
    print("Somthing else went wrong")
else:
    print("nothing")


try:
    print("hello")
except:
    print("Somthing else went wrong")
finally:
    print("f")
