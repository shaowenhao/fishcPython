Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """魔法方法"""
'魔法方法'
>>> class CapStr(str):
	def __new__(cls,string):
		string = string.upper()
		return super().__new__(cls,string)

	
>>> CapStr.__dict__
mappingproxy({'__module__': '__main__', '__new__': <staticmethod object at 0x00000284CE88AB50>, '__dict__': <attribute '__dict__' of 'CapStr' objects>, '__weakref__': <attribute '__weakref__' of 'CapStr' objects>, '__doc__': None})
>>> 
>>> CapStr.mor()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    CapStr.mor()
AttributeError: type object 'CapStr' has no attribute 'mor'
>>> CapStr.mro()
[<class '__main__.CapStr'>, <class 'str'>, <class 'object'>]
>>> cs = CapStr("FishC")
>>> cs
'FISHC'
>>> cs.lower()
'fishc'
>>> 
>>> 
>>> """ __del__(self) """
' __del__(self) '
>>> 
>>> class C:
	def __init__(self):
		print("我来了")
	def __del__(self):
		print("我走了")

		
>>> c = C()
我来了
>>> del c
我走了
>>> 
>>> 