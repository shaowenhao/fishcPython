Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """绑定2 剩余内容"""
'绑定2 剩余内容'
>>> 
>>> class A:
	def __init__(self):
		print("哈喽 我还是A")

		
>>> class B1(A):
	def __init__(self):
		A.__init__(self)
		print("哈喽 我是B1")

		
>>> class B2(A):
	def __init__(self):
		A.__init__(self)
		print("哈喽 我是B2")

		
>>> class C(B1,B2):
	def __init__(self):
		B1.__init__(self)
		B2.__init__(self)
		print("哈喽 我是C")

		
>>> c = C()
哈喽 我还是A
哈喽 我是B1
哈喽 我还是A
哈喽 我是B2
哈喽 我是C
>>> 
>>> """钻石继承"""
'钻石继承'
>>> 
>>> """super"""
'super'
>>> 
>>> """MRO 类的方法解析顺序，super避免重复初始化"""
'MRO 类的方法解析顺序，super避免重复初始化'
>>> C.mro()
[<class '__main__.C'>, <class '__main__.B1'>, <class '__main__.B2'>, <class '__main__.A'>, <class 'object'>]
>>> B1.mro()
[<class '__main__.B1'>, <class '__main__.A'>, <class 'object'>]
>>> A.mro()
[<class '__main__.A'>, <class 'object'>]
>>> 
>>> class B1(A):
	def __init__(self):
		super().__init__()
		print("哈喽 我是B1")

		
>>> class B2(A):
	def __init__(self):
		super().__init__()
		print("哈喽 我是B2")

		
>>> class C(B1,B2):
	def __init__(self):
		super().__init__()
		print("哈喽 我是C")

		
>>> c = C()
哈喽 我还是A
哈喽 我是B2
哈喽 我是B1
哈喽 我是C
>>> 