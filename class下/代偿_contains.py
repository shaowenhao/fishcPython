Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """__contains__(self,item)魔法方法 主要用于实现成员关系的检查"""
'__contains__(self,item)魔法方法 主要用于实现成员关系的检查'
>>> """对应的运算符是 in 和 not in """
'对应的运算符是 in 和 not in '
>>> 
>>> class C:
	def __init__(self,data):
		self.data = data
	def __contains__(self,item):
		print("HI")
		return item in self.data

	
>>> c = C([1,2,3,4,5])
>>> 
>>> 3 in c
HI
True
>>> 
>>> 