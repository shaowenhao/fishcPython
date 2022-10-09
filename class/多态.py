Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """多态"""
'多态'
>>> class Shape:
	def __init__(self,name):
		self.name =  name
	def area(slef):
		pass

	
>>> class Square(Shape):
	def __init__(self,length):
		super().__init__("正方形")
		self.length = length
	def area(slef):
		return self.length * self.length

	
>>> 