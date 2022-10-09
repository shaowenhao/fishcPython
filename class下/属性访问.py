Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """属性访问"""
'属性访问'
>>> 
>>> class C:
	def __init__(self,name,age):
		self.name = name
		self.__age = age

		
>>> c = C("小甲鱼",18)
>>> 
>>> hasattr(c,"name")
True
>>> getattr(c,"name")
'小甲鱼'
>>> 
>>> getattr(c,"_C__age")
18
>>> setattr(c,"_C__age",19)
>>> 
>>> getattr(c,"_C__age")
19
>>> 
>>> 