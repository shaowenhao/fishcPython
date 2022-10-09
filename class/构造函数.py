Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """类和对象 之 构造函数"""
'类和对象 之 构造函数'
>>> 
>>> """构造函数 __init__() """
'构造函数 __init__() '
>>> class C:
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def add(self):
		return self.x + self.y
	def mul(self):
		return self.x * self.y

	
>>> c = C(2,3)
>>> c.add()
5
>>> c.mul()
6
>>> 