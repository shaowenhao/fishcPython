Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """ 类方法"""
' 类方法'
>>> 
>>> """@classMethod装饰器"""
'@classMethod装饰器'
>>> 
>>> class C:
	def funA(self):
		print(self)
	@classmethod
	def funB(cls):
		print(cls)

		
>>> """self cls都是约定俗成的"""
'self cls都是约定俗成的'
>>> 
>>> c = C()
>>> c.funA()
<__main__.C object at 0x000001FF5B406A90>
>>> 
>>> c.funB()
<class '__main__.C'>
>>> 
>>> 
>>> class C:
	count = 0
	def __init__(self):
		C.count += 1
	@classmethod
	def get_count(cls):
		print(f"该类一共实例化了{cls.count}个对象")

		
>>> c1 = C()
>>> c2 = C()
>>> c3 = C()
>>> c3.get_count()
该类一共实例化了3个对象
>>> 
>>> C.get_count()
该类一共实例化了3个对象
>>> 
>>> 
>>> """静态方法"""
'静态方法'
>>> 
>>> class C:
	@staticmethod
	def funC():
		print("I love FishC.")

		
>>> c =C()
>>> c.funC()
I love FishC.
>>> C.funC()
I love FishC.
>>> 
>>> 
>>> """静态方法不需要绑定"""
'静态方法不需要绑定'
>>> 
>>> 
>>> """涉及继承问题的 统计问题"""
'涉及继承问题的 统计问题'
>>> 
>>> class C:
	count = 0
	@classmethod
	def add(cls):
		cls.count += 1
	def __init__(self):
		self.add()
	@classmethod
	def get_count(cls):
		print(f"该类一共实例化了{cls.count}个对象")

		
>>> class D(C):
	count = 0

	
>>> c1 = C()
>>> d1, d2 = D(),D()
>>> c1.get_count()
该类一共实例化了1个对象
>>> d1.get_count()
该类一共实例化了2个对象
>>> D.get_count()
该类一共实例化了2个对象
>>> C.get_count()
该类一共实例化了1个对象
>>> 