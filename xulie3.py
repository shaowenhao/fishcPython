Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """序列下 all() any() """
'序列下 all() any() '
>>> x = [1,1,0]
>>> y= [1,1,9]
>>> 
>>> all(x)
False
>>> all(y)
True
>>> 
>>> any(x)
True
>>> 
>>> any(y)
True
>>> 
>>> seasons = ["Spring","Summer","Fall","Winter"]
>>> 
>>> enumerate(seasons)
<enumerate object at 0x0000026DEBD9B840>
>>> 
>>> 
>>> list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
>>> 
>>> list(enumerate(seasons,10))
[(10, 'Spring'), (11, 'Summer'), (12, 'Fall'), (13, 'Winter')]
>>> 
>>> x = [1,2,3]
>>> y = [4,5,6]
>>> zipped = zip(x,y)
>>> list(zipped)
[(1, 4), (2, 5), (3, 6)]
>>> 
>>> 
>>> z = "FishC"
>>> zipped = zip(x,y,z)
>>> list(zipped)
[(1, 4, 'F'), (2, 5, 'i'), (3, 6, 's')]
>>> 
>>> import itertools
>>> zipped = itertools.zip_longest(x,y,z)
>>> list(zipped)
[(1, 4, 'F'), (2, 5, 'i'), (3, 6, 's'), (None, None, 'h'), (None, None, 'C')]
>>> 
>>> #map()函数
>>> 
>>> 
>>> mapped = maop(ord,"FishC")
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    mapped = maop(ord,"FishC")
NameError: name 'maop' is not defined
>>> mapped = map(ord,"FishC")
>>> list(mapped)
[70, 105, 115, 104, 67]
>>> 
>>> mapped = map(pow,[2,3,10],[5,2,3])
>>> list(mapped)
[32, 9, 1000]
>>> # 做了指数操作
>>> 
>>> 
>>> 
>>> #filter函数
>>> 
>>> list(filter(str.islower,"FishC"))
['i', 's', 'h']
>>> 
>>> #迭代器和  可迭代对象
>>> #迭代器和  可迭代对象
>>> 
>>> 
>>> mapped = map(ord,"FishC")
>>> #结果是迭代器
>>> for each in mapped:
	print(each)

	
70
105
115
104
67
>>> 
>>> list(mapped)
[]
>>> #迭代器不可以重复使用
>>> 
>>> 
>>> # iter()
>>> 
>>> x = [1,2,3]
>>> y = iter(x)
>>> type(x)
<class 'list'>
>>> type(y)
<class 'list_iterator'>
>>> 
>>> 
>>> # next()
>>> 
>>> next(y)
1
>>> next(y)
2
>>> next(y)
3
>>> next(y)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    next(y)
StopIteration
>>> 
>>> z = iter(x)
>>> next(z,"nothing else")
1
>>> next(z,"nothing else")
2
>>> next(z,"nothing else")
3
>>> next(z,"nothing else")
'nothing else'
>>> 
>>> 