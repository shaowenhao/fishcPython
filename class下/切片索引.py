Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """ 类和对象 索引 切片"""
' 类和对象 索引 切片'
>>> 
>>> class C:
	def __getitem__(self,index):
		print(index)

		
>>> c = C()
>>> c[2]
2
>>> 
>>> c[2:8]
slice(2, 8, None)
>>> 
>>> s = "I love FishC"
>>> 
>>> s[2:6]
'love'
>>> s[slice(2,6)]
'love'
>>> 
>>> s[7:]
'FishC'
>>> 
>>> s[slice(7,None)]
'FishC'
>>> 
>>> s[::4]
'Ivi'
>>> 
>>> s[slice(None,None,4)]
'Ivi'
>>> 
>>> 
>>> 
>>> 
>>> class D:
	def __init__(self,data):
		self.data = data
	def __getitem__(self,index):
		return self.data[index]
        def __setitem__(self,index,value):
		
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> class D:
	def __init__(self,data):
		self.data = data
	def __getitem__(self,index):
		return self.data[index]
	def __setitem__(self,index,value):
		self.data[index] = value

		
>>> d = D([1,2,3,4,5])
>>> d[1]
2
>>> d[1] = 6
>>> d
<__main__.D object at 0x00000271D36DA3D0>
>>> d[1]
6
>>> d[:]
[1, 6, 3, 4, 5]
>>> 
>>> 
>>> 
>>> 
>>> class D:
	def __init__(self,data):
		self.data = data
	def __getitem__(self,index):
		return self.data[index] * 2

	
>>> d = D([1,2,3,4,5])
>>> for i in d:
	print(i,end=' ')

	
2 4 6 8 10 
>>> for i in d:
	print(i,end=',')

	
2,4,6,8,10,
>>> 
>>> 
>>> x = [1,2,3,4,5]
>>> dir(x)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> 
>>> 
>>> next(x)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    next(x)
TypeError: 'list' object is not an iterator
>>> 
>>> for i in x:
	print(i,end=' ')

	
1 2 3 4 5 
>>> _ = iter(x)
>>> while True:
	try:
		i = _.__next__()
	except SopIteration:
		break
	print(i,end=' ')

	
1 2 3 4 5 Traceback (most recent call last):
  File "<pyshell#72>", line 3, in <module>
    i = _.__next__()
StopIteration

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#72>", line 4, in <module>
    except SopIteration:
NameError: name 'SopIteration' is not defined
>>> while True:
	try:
		i = _.__next__()
	except StopIteration:
		break
	print(i,end=' ')

	
>>> x
[1, 2, 3, 4, 5]
>>> 
>>> 
>>> _ = iter(x)
>>> _
<list_iterator object at 0x00000271D364C2B0>
>>> while True:
	try:
		i = _.__next__()
	except StopIteration:
		break
	print(i,end=' ')

	
1 2 3 4 5 
>>> 
>>> x
[1, 2, 3, 4, 5]
>>> type(x)
<class 'list'>
>>> type(_)
<class 'list_iterator'>
>>> 