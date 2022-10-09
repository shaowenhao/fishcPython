Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """ 私有变量 """
' 私有变量 '
>>> 
>>> """ 没有办法做到真正的私有化"""
' 没有办法做到真正的私有化'
>>> 
>>> class C:
	def __init__(self,x):
		self.__x = x
	def set_x(self,x):
		self.__x = x
	def get_x(self):
		print(self.__x)

		
>>> c = C(250)
>>> c.__x
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    c.__x
AttributeError: 'C' object has no attribute '__x'
>>> c.get__x()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    c.get__x()
AttributeError: 'C' object has no attribute 'get__x'
>>> c.get_x()
250
>>> c.set_x(520)
>>> c.get_x()
520
>>> 
>>> 
>>> """但是就是像一条路走到黑"""
'但是就是像一条路走到黑'
>>> c.__dict__
{'_C__x': 520}
>>> c._C__x
520
>>> 
>>> 
>>> """方法名同理"""
'方法名同理'
>>> 
>>> 