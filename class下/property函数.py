Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """ property函数 """
' property函数 '
>>> 
>>> class C:
	def __init__(self):
		self._x = 250
	def getx(self):
		return self._x
	def setx(self,value):
		self._x = value
	def delx(self):
		del self._x
	x =property(getx,setx,delx)

	
>>> c = C()
>>> 
>>> c.x
250
>>> 
>>> c.x = 520
>>> 
>>> c.__dict__
{'_x': 520}
>>> 
>>> del c.x
>>> c.__dict__
{}
>>> 
>>> 