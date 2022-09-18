Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """ 函数 3 """
' 函数 3 '
>>> 
>>> print("小甲鱼","爱","编程")
小甲鱼 爱 编程
>>> 
>>> #收集参数
>>> 
>>> def myfunc(*args):
	print("有{}个参数".format(len(args)))
	print("第二个参数是：{}".format(args[1]))

	
>>> myfunc("小甲鱼","哈哈哈")
有2个参数
第二个参数是：哈哈哈
>>> 
>>> 
>>> def myfunc(*args):
	print(args)

	
>>> myfunc(1,2,3,4,5)
(1, 2, 3, 4, 5)
>>> 
>>> 
>>> 
>>> def myfunc():
	return 1,2,3

>>> myfunc()
(1, 2, 3)
>>> 
>>> 
>>> def myfunc(*args):
	print(type(args))

	
>>> myfunc(1,2,3)
<class 'tuple'>
>>> 
>>> 
>>> def myfunc(**kwargs):
	print(kwargs)

	
>>> myfunc(a=1,b=2,c=3)
{'a': 1, 'b': 2, 'c': 3}
>>> 
>>> #拆成字典
>>> 
>>> 
>>> myfunc(a,*b,**c):
	
SyntaxError: invalid syntax
>>> def myfunc(a,*b,**c):
	print(a,b,c)

	
>>> myfunc(1,2,3,4,x=5,y=6)
1 (2, 3, 4) {'x': 5, 'y': 6}
>>> 
>>> 
>>> #解包参数
>>> 
>>> args = (1,2,3,4)
>>> def myfunc(a,b,c,d):
	print(a,b,c,d)

	
>>> myfunc(args)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    myfunc(args)
TypeError: myfunc() missing 3 required positional arguments: 'b', 'c', and 'd'
>>> myfunc(*args)
1 2 3 4
>>> 
>>> 
>>> kwargs = {'a':1,'b':2,'c':3,'d':4}
>>> myfunc(**kwargs)
1 2 3 4
>>> 
>>> 