Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """函数"""
'函数'
>>> 
>>> def myfunc(s,vt,o):
	return "".join((o,vt,s))

>>> myfunc("我","爱","你")
'你爱我'
>>> 
>>> 
>>> # 关键字参数
>>> 
>>> myfunc(o="我",vt="爱",s="你")
'我爱你'
>>> 
>>> 
>>> #默认参数
>>> 
>>> def myfunc(s,vt,o="小甲鱼"):
	return "".join((o,vt,s))

>>> myfunc("香蕉","吃")
'小甲鱼吃香蕉'
>>> 
>>> help(sum)
Help on built-in function sum in module builtins:

sum(iterable, /, start=0)
    Return the sum of a 'start' value (default: 0) plus an iterable of numbers
    
    When the iterable is empty, return the start value.
    This function is intended specifically for use with numeric values and may
    reject non-numeric types.

>>> help(abc)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    help(abc)
NameError: name 'abc' is not defined
>>> help(abs)
Help on built-in function abs in module builtins:

abs(x, /)
    Return the absolute value of the argument.

>>> # /斜杠左边的参数表示 只能用位置参数 不能用关键字参数
>>> 
>>> abs(-1.5)
1.5
>>> 
>>> abs(x = -1.5)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    abs(x = -1.5)
TypeError: abs() takes no keyword arguments
>>> 
>>> sum([1,2,3],4)
10
>>> 
>>> sum([1,2,3],start=4)
10
>>> 
>>> # * 星号左边的 两种参数都可以，右边只能是关键字参数
>>> 
>>> def abc(a,*,b,c):
	print(a,b,c)

	
>>> abc(1,2,3)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    abc(1,2,3)
TypeError: abc() takes 1 positional argument but 3 were given
>>> 
>>> abc(1,b=2,c=3)
1 2 3
>>> 
>>> 