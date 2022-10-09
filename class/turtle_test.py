Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """类 对象"""
'类 对象'
>>> 
>>> class Turtle:
	head = 1
	eyes = 2
	legs = 4

	
>>> 
=================== RESTART: D:/py_workspace/class/turtle.py ===================
>>> t1 = Turtle()
>>> t1.head
1
>>> t1.run()
turtle run
>>> t1
<__main__.Turtle object at 0x000001E7057FC2B0>
>>> t1.mouth = 1
>>> t1.mouth
1
>>> 
>>> dir(t1)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'eat', 'eyes', 'head', 'legs', 'mouth', 'run']
>>> 
>>> x = 520
>>> type(x)
<class 'int'>
>>> 
>>> y = "FishC"
>>> type(y)
<class 'str'>
>>> 
>>> 
>>> class C:
	def hello():
		print("hello")

		
>>> c1 = C()
>>> c1.hello()
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    c1.hello()
TypeError: hello() takes 0 positional arguments but 1 was given
>>> 
>>> class C:
	def get_self(self):
		print(self)

		
>>> c2 = C()
>>> c2.get_Self()
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    c2.get_Self()
AttributeError: 'C' object has no attribute 'get_Self'
>>> c2.get_self()
<__main__.C object at 0x000001E70588ABE0>
>>> c2
<__main__.C object at 0x000001E70588ABE0>
>>> """传递给方法的 是实例对象本身"""
'传递给方法的 是实例对象本身'
>>> 
>>> """默认的第一个参数self"""
'默认的第一个参数self'
>>> 