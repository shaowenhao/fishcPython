Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """继承"""
'继承'
>>> 
>>> class A:
	x = 520
	def hello(self):
		print("hello i am A")

		
>>> class B(A):
	pass

>>> """表示B 继承 A"""
'表示B 继承 A'
>>> 
>>> b = B();
>>> b.x
520
>>> b.hello()
hello i am A
>>> 
>>> 
>>> class B(A):
	x = 880
	def hello(self):
		print("hello i am B")

		
>>> b2 = B()
>>> b2.x
880
>>> b2.hello()
hello i am B
>>> 
>>> """isinstance() 判断是否属于某个类"""
'isinstance() 判断是否属于某个类'
>>> isinstance(b2,B)
True
>>> isinstance(b2,A)
True
>>> 
>>> """issubclass()"""
'issubclass()'
>>> issubclass(B,A)
True
>>> 
>>> """多重继承"""
'多重继承'
>>> 
>>> class B:
	x = 880
	y = 250
	def hello(self):
		print("i am B")

		
>>> class C(A,B):
	pass

>>> c = C()
>>> c.x
520
>>> c.hello()
hello i am A
>>> """从左往右执行 先看A"""
'从左往右执行 先看A'
>>> c.y
250
>>> 
>>> """组合"""
'组合'
>>> 
>>> class Cat:
	def say(self):
		print("喵喵喵")

		
>>> class Dog:
	def say(self):
		print("旺旺")

		
>>> class Garden:
	c = Cat()
	d = Dog()
	def Say(self):
		self.c.say()
		self.d.say()

		
>>> g = Garden()
>>> g.say()
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    g.say()
AttributeError: 'Garden' object has no attribute 'say'
>>> g.Say()
喵喵喵
旺旺
>>> 