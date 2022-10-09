Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """ 运算相关的魔法方法"""
' 运算相关的魔法方法'
>>> class S(str):
	def __add__(self,other):
		return len(self) + len(other)

	
>>> S.__dict__
mappingproxy({'__module__': '__main__', '__add__': <function S.__add__ at 0x000001569EC19CA0>, '__dict__': <attribute '__dict__' of 'S' objects>, '__weakref__': <attribute '__weakref__' of 'S' objects>, '__doc__': None})
>>> S.__dir__
<method '__dir__' of 'object' objects>
>>> str.__init__
<slot wrapper '__init__' of 'object' objects>
>>> a = str.__init__("abc")
>>> a
>>> s1 = S("abc")
>>> s1
'abc'
>>> a2 = str("abc")
>>> a2
'abc'
>>> s2 = S("def")
>>> s1 + s2
6
>>> """魔法方法的作用 就是拦截 """
'魔法方法的作用 就是拦截 '
>>> 
>>> 