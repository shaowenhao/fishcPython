Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """作用域"""
'作用域'
>>> def myfunc():
	x = 520
	print(x)

	
>>> myfunc()
520
>>> 
>>> x = 880
>>> def myfunc():
	print(x)

	
>>> myfunc()
880
>>> 
>>> # global语句
>>> 
>>> x = 880
>>> 
>>> def myfunc():
	global x
	x = 520
	print(x)

	
>>> myfunc()
520
>>> 
>>> print(x)
520
>>> 
>>> # 可以修改全局变量 不提倡
>>> 
>>> #嵌套函数
>>> 
>>> def funA():
	x = 520
	def funB():
		x = 880
		print("In funB, x =",x)
	print("In funA, x =",x)

	
>>> def funA():
	x = 520
	def funB():
		x = 880
		print("In funB, x =",x)
	funB()
	print("In funA, x =",x)

	
>>> funA()
In funB, x = 880
In funA, x = 520
>>> 
>>> #nonlocal语句
>>> 
>>> 
>>> 
>>> 
>>> def funA():
	x = 520
	def funB():
		nonlocal x = 880
		print("In funB, x =",x)
	funB()
	print("In funA, x =",x)
	
SyntaxError: invalid syntax
>>> 
>>> def funA():
	x = 520
	def funB():
		nonlocal x
		x = 880
		print("In funB, x =",x)
	funB()
	print("In funA, x =",x)

	
>>> funcA()
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    funcA()
NameError: name 'funcA' is not defined
>>> funA()
In funB, x = 880
In funA, x = 880
>>> 
>>> 
>>> #LEGB 规则
>>> # Local Enclosed Global Build-In
>>> 
>>> str = "aaaa"
>>> str(520)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    str(520)
TypeError: 'str' object is not callable
>>> # G 覆盖 B
>>> #取名规范 ！！
>>> 