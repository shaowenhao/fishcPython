Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """ 描述符 """
' 描述符 '
>>> 
>>> """ 实现了 一个或多个 方法的类叫做描述符 """
' 实现了 一个或多个 方法的类叫做描述符 '
>>> """__get__(self,instance,owner),__set__(self,instance,value),__delete__(self,instance) """
'__get__(self,instance,owner),__set__(self,instance,value),__delete__(self,instance) '
>>> 
>>> 
>>> class D:
	def __get__(seld,instance,owner):
		print(f"get\n self -> {self}\ninstance ->{instance}\nowner->{owner}")
	def __set__(self,instance,value):
		print(f"set\n self -> {self}\ninstance ->{instance}\nvalue->{value}")
	def __delete__(self,instance):
		print(f"delete\nself->{self}\ninstance->{instance}")

		
>>> c = C()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    c = C()
NameError: name 'C' is not defined
>>> class C:
	x = D()

	
>>> c =C()
>>> c.x = 250
set
 self -> <__main__.D object at 0x00000225A80E1BE0>
instance -><__main__.C object at 0x00000225A8DFD2B0>
value->250
>>> 
>>> c.x
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    c.x
  File "<pyshell#13>", line 3, in __get__
    print(f"get\n self -> {self}\ninstance ->{instance}\nowner->{owner}")
NameError: name 'self' is not defined
>>> 
>>> 
>>> class D:
	def __get__(self,instance,owner):
		print(f"get\n self -> {self}\ninstance ->{instance}\nowner->{owner}")
	def __set__(self,instance,value):
		print(f"set\n self -> {self}\ninstance ->{instance}\nvalue->{value}")
	def __delete__(self,instance):
		print(f"delete\nself->{self}\ninstance->{instance}")

		
>>> c = C()
>>> c.x
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    c.x
  File "<pyshell#13>", line 3, in __get__
    print(f"get\n self -> {self}\ninstance ->{instance}\nowner->{owner}")
NameError: name 'self' is not defined
>>> c.x = 250
set
 self -> <__main__.D object at 0x00000225A80E1BE0>
instance -><__main__.C object at 0x00000225A8E8A3D0>
value->250
>>> c.x
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    c.x
  File "<pyshell#13>", line 3, in __get__
    print(f"get\n self -> {self}\ninstance ->{instance}\nowner->{owner}")
NameError: name 'self' is not defined
>>> 
>>> c = C()
>>> c.x =250
set
 self -> <__main__.D object at 0x00000225A80E1BE0>
instance -><__main__.C object at 0x00000225A8E9D370>
value->250
>>> 
>>> c.x
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    c.x
  File "<pyshell#13>", line 3, in __get__
    print(f"get\n self -> {self}\ninstance ->{instance}\nowner->{owner}")
NameError: name 'self' is not defined
>>> 
>>> del c.x
delete
self-><__main__.D object at 0x00000225A80E1BE0>
instance-><__main__.C object at 0x00000225A8E9D370>
>>> File "<pyshell#29>", line 1, in <module>
SyntaxError: invalid syntax
>>> D.__dirt__
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    D.__dirt__
AttributeError: type object 'D' has no attribute '__dirt__'
>>> D.__dict__
mappingproxy({'__module__': '__main__', '__get__': <function D.__get__ at 0x00000225A8F32310>, '__set__': <function D.__set__ at 0x00000225A8F323A0>, '__delete__': <function D.__delete__ at 0x00000225A8F32430>, '__dict__': <attribute '__dict__' of 'D' objects>, '__weakref__': <attribute '__weakref__' of 'D' objects>, '__doc__': None})
>>> 
>>> 
>>> 
>>> 
>>> 
>>> class D:
	def __get__(self,instance,owner):
		print(f"get\n self -> {self}\ninstance ->{instance}\nowner->{owner}")
	def __set__(self,instance,value):
		print(f"set\n self -> {self}\ninstance ->{instance}\nvalue->{value}")
	def __delete__(self,instance):
		print(f"delete\nself->{self}\ninstance->{instance}")

		
>>> class C:
	x = D()

	
>>> c = C()
>>> c.x = 250
set
 self -> <__main__.D object at 0x00000225A8E9DA60>
instance -><__main__.C object at 0x00000225A8E9D160>
value->250
>>> c.x
get
 self -> <__main__.D object at 0x00000225A8E9DA60>
instance -><__main__.C object at 0x00000225A8E9D160>
owner-><class '__main__.C'>
>>> del c.x
delete
self-><__main__.D object at 0x00000225A8E9DA60>
instance-><__main__.C object at 0x00000225A8E9D160>
>>> 