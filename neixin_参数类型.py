Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """ 函数文档"""
' 函数文档'
>>> 
>>> def times(s:str, n:int) -> str:
	rerurn s * n
	
SyntaxError: invalid syntax
>>> 
>>> def times(s:str, n:int) -> str:
	return s * n

>>> times("hello",3)
'hellohellohello'
>>> 
>>> def times(s:list, n:int = 3) -> list:
	return s * n

>>> times([1,2,3])
[1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> 
>>> 
>>> def times(s:list[int], n:int = 3) -> list:
	return s * n

>>> """ 参数类型"""
' 参数类型'
>>> 
>>> 
>>> """内省"""
'内省'
>>> 
>>> times.__annotations__
{'s': list[int], 'n': <class 'int'>, 'return': <class 'list'>}
>>> 
>>> print.__doc__
"print(value, ..., sep=' ', end='\\n', file=sys.stdout, flush=False)\n\nPrints the values to a stream, or to sys.stdout by default.\nOptional keyword arguments:\nfile:  a file-like object (stream); defaults to the current sys.stdout.\nsep:   string inserted between values, default a space.\nend:   string appended after the last value, default a newline.\nflush: whether to forcibly flush the stream."
>>> print(print.__doc__)
print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

Prints the values to a stream, or to sys.stdout by default.
Optional keyword arguments:
file:  a file-like object (stream); defaults to the current sys.stdout.
sep:   string inserted between values, default a space.
end:   string appended after the last value, default a newline.
flush: whether to forcibly flush the stream.
>>> 