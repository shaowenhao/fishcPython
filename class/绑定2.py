Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """ 绑定"""
' 绑定'
>>> 
>>> class C:
	def set_x(self,,v):
		
SyntaxError: invalid syntax
>>> class C:
	def set_x(self,v):
		self.x = v

		
>>> c =  C()
>>> c.__dict__
{}
>>> c.set_x(250)
>>> c.__dict__
{'x': 250}
>>> 
>>> c.x
250
>>> 
>>> 
>>> """把类当字典使用"""
'把类当字典使用'
>>> class C:
	pass

>>> C.x = 250
>>> C.y = "小甲鱼"
>>> C.z = [1,2,3]
>>> print(C.x)
250
>>> print(C.y)
小甲鱼
>>> print(C.z)
[1, 2, 3]
>>> 
>>> d = {}
>>> d['x'] = 250
>>> d['z'] = [1,2,3]
>>> print(d['x'])
250
>>> print(d['z'])
[1, 2, 3]
>>> 
>>>




