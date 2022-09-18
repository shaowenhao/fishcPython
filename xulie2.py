Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """和序列相关的一些函数 """
'和序列相关的一些函数 '
>>> 
>>> # 列表元组和字符串相互转换
>>> # list() tuple() str()
>>> 
>>> lis("FishC")
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    lis("FishC")
NameError: name 'lis' is not defined
>>> list("FishC")
['F', 'i', 's', 'h', 'C']
>>> 
>>> list((1,2,3,4,5))
[1, 2, 3, 4, 5]
>>> 
>>> tuple("FishC")
('F', 'i', 's', 'h', 'C')
>>> 
>>> 
>>> tuple([1,2,3,4,5])
(1, 2, 3, 4, 5)
>>> 
>>> 
>>> str((1,2,3))
'(1, 2, 3)'
>>> 
>>> 
>>> # min() & max()
>>> 
>>> s = [1,1,2,3,5]
>>> 
>>> min(s)
1
>>> 
>>> t = "FishC"
>>> max(t)
's'
>>> 
>>> s = []
>>> 
>>> min(s,"nothing!!!!")
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    min(s,"nothing!!!!")
TypeError: '<' not supported between instances of 'str' and 'list'
>>> 
>>> min(s,default="nothing!!!!")
'nothing!!!!'
>>> 
>>> min(1,2,3)
1
>>> 
>>> #len() & sum()
>>> len(range(0,10))
10
>>> range(0,10)
range(0, 10)
>>> i = range(0.10)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    i = range(0.10)
TypeError: 'float' object cannot be interpreted as an integer
>>> 
>>> for i in range(0,10):
	print(i)

	
0
1
2
3
4
5
6
7
8
9
>>> s = [1,0,0,8,6]
>>> sum(s)
15
>>> 
>>> # sorted() & reversed()
>>> 
>>> s = [1,2,3,0,6]
>>> sorted(s)
[0, 1, 2, 3, 6]
>>> 
>>> sorted(s,reverse=True)
[6, 3, 2, 1, 0]
>>> 
>>> 
>>> t = ["FishC","Apple","Book","Banana","Pen"]
>>> 
>>> sorted(t)
['Apple', 'Banana', 'Book', 'FishC', 'Pen']
>>> 
>>> sorted(t,key=len)
['Pen', 'Book', 'FishC', 'Apple', 'Banana']
>>> 
>>> #列表的sort方法 只能处理列表
>>> t.sort(key=len)
>>> 
>>> t
['Pen', 'Book', 'FishC', 'Apple', 'Banana']
>>> 
>>> #sorted函数强大 可以作用 字符串 和元组
>>> sorted("FishC")
['C', 'F', 'h', 'i', 's']
>>> 
>>> sorted((1,0,0,,6))
SyntaxError: invalid syntax
>>> sorted((1,0,0,8,6))
[0, 0, 1, 6, 8]
>>> 
>>> 
>>> s = [1,2,5,8,0]
>>> reversed(s)
<list_reverseiterator object at 0x0000024FA59DB580>
>>> 
>>> list(reversed(s))
[0, 8, 5, 2, 1]
>>> s.reverse()
>>> s
[0, 8, 5, 2, 1]
>>> 
>>> list(reversed(range(0,10)))
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
>>> 