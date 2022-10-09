Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """ call 魔法方法 """
' call 魔法方法 '
>>> 
>>> class C:
	def __call__(self):
		print("Hi)
		      
SyntaxError: EOL while scanning string literal
>>> class C:
	def __call__(self):
		print("Hi")

		
>>> c = C()
>>> 
>>> c()
Hi
>>> 
>>> class C:
	def __call__(self,*args,**kwargs):
		print(f"位置参数->{args}\n关键字参数->{kwargs}")

		
>>> c = C()
>>> c(1,2,3,x=250,y=520)
位置参数->(1, 2, 3)
关键字参数->{'x': 250, 'y': 520}
>>> 
>>> """call可以实现 闭包函数的功能"""
'call可以实现 闭包函数的功能'
>>> 
>>> class Power:
	def __init__(self,exp):
		self.exp = exp
	def __call__(self,base):
		return base ** self.exp

	
>>> """call的实现让对象可以像方法一样被调用"""
'call的实现让对象可以像方法一样被调用'
>>> square = Power(2)
>>> square(5)
25
>>> 
>>>


