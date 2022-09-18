Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """lambda表达式"""
'lambda表达式'
>>> 
>>> def squarex(x):
	return x * x

>>> square(3)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    square(3)
NameError: name 'square' is not defined
>>> squarex(3)
9
>>> 
>>> lambda y :y * y
<function <lambda> at 0x000001F704DB8D30>
>>> squareY = lambda y : y * y
>>> 
>>> squareY(3)
9
>>> 
>>> y = [lambda x : x * x,2,3]
>>> y[0](y[1])
4
>>> 
>>> mapped = map(lambda x :ord(x) + 10, "FishC")
>>> mapped
<map object at 0x000001F704DAAFD0>
>>> 
>>> list(mapped)
[80, 115, 125, 114, 77]
>>> 
>>> def boring(x):
	return ord(x) + 10

>>> list(map(boring,"FishC"))
[80, 115, 125, 114, 77]
>>> 
>>> 
>>> list(filter(lambda x :x % 2, range(10)))
[1, 3, 5, 7, 9]
>>> 
>>> 