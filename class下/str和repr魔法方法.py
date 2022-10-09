Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """__str__(self) 和 __repr__(self) """
'__str__(self) 和 __repr__(self) '
>>> 
>>> str(123)
'123'
>>> 
>>> repr(123)
'123'
>>> 
>>> str("FishC")
'FishC'
>>> 
>>> repr("FishC")
"'FishC'"
>>> 
>>> "多穿了个外套"
'多穿了个外套'
>>> 
>>> eval("1 + 2")
3
>>> """ 参数去引号执行"""
' 参数去引号执行'
>>> 
>>> eval(str("FishC"))
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    eval(str("FishC"))
  File "<string>", line 1, in <module>
NameError: name 'FishC' is not defined
>>> 
>>> eval(repr("FishC"))
'FishC'
>>> 
>>> 
>>> """ 了解完函数 看看魔法方法"""
' 了解完函数 看看魔法方法'
>>> 
>>> class C:
	def __repr__(self):
		return "I love FishC"

	
>>> c = C()
>>> 
>>> repr(c)
'I love FishC'
>>> 
>>> str(c)
'I love FishC'
>>> 
>>> """ 该魔法方法也可以作为str函数的 代偿"""
' 该魔法方法也可以作为str函数的 代偿'
>>> 
>>> 
>>> cs = [C(),C(),C()]
>>> for each in cs:
	print(each)

	
I love FishC
I love FishC
I love FishC
>>> 
>>> print(cs)
[I love FishC, I love FishC, I love FishC]
>>> 
>>> """__repr__(self)实现的类 可以打印列表"""
'__repr__(self)实现的类 可以打印列表'
>>> 
>>> 