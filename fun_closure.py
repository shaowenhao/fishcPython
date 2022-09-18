Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> """闭包函数"""
'闭包函数'
>>> 
>>> 
>>> def funA():
	x = 880
	def funB():
		print(x)

		
>>> funA()
>>> 
>>> def funA():
	x = 880
	def funB():
		print(x)
	funB()

	
>>> funA()
880
>>> 
>>> #嵌套函数 调到funB的方式 执行 funA
>>> 
>>> 
>>> #把函数作为返回值 只需要 return 函数名
>>> 
>>> def funA():
	x = 880
	def funB():
		print(x)
	return funB

>>> funA()
<function funA.<locals>.funB at 0x000002B2A66B88B0>
>>> funA()()
880
>>> 
>>> #不通过funA 调用
>>> 
>>> funny = funA()
>>> funny()
880
>>> 
>>> # LEGB中的E 嵌套函数， 外层函数的作用域 在函数执行完 以某种形式保存下来
>>> 
>>> 
>>> 
>>>  def power(exp):
	 
SyntaxError: unexpected indent
>>> def power(exp):
	def exp_of(base):
		return base ** exp
	return exp_of

>>> square = power(2)
>>> square(2)
4
>>> square(5)
25
>>> 
>>> cube = power(3)
>>> cube(2)
8
>>> cube(5)
125
>>> 
>>> # 这里power类似工厂函数 给不同的参数不同的结果
>>> 
>>> # nolocal语句 可以让嵌套函数的内层语句修改外层变量
>>> 
>>> def outer():
	x = 0
	y = 0
	def inner(x1,y1):
		nonlocal x,y
		x += x1
		y += y1
		print(f"现在,x = {x}, y = {y}")

		
>>> def outer():
	x = 0
	y = 0
	def inner(x1,y1):
		nonlocal x,y
		x += x1
		y += y1
		print(f"现在,x = {x}, y = {y}")
	return inner

>>> move = outer()
>>> move(1,2)
现在,x = 1, y = 2
>>> move(-2,2)
现在,x = -1, y = 4
>>> 
>>> 
>>> #1. 利用嵌套函数的外层作用域具有记忆能力的这个特性
>>> #2. 将内层函数作为返回值给返回
>>> 