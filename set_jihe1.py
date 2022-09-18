Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """集合"""
'集合'
>>> 
>>> type({})
<class 'dict'>
>>> 
>>> type({"one})
      
SyntaxError: EOL while scanning string literal
>>> type({"one"})
<class 'set'>
>>> 
>>> type({"one":1})
<class 'dict'>
>>> 
>>> # 集合中所有元素独一无二 无序
>>> 
>>> {"FishC","Python"}
{'Python', 'FishC'}
>>> 
>>> {s for s in "Fishc"}
{'s', 'i', 'h', 'c', 'F'}
>>> 
>>> set("FishC")
{'s', 'i', 'h', 'C', 'F'}
>>> 
>>> #无法用下标
>>> s[0]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    s[0]
NameError: name 's' is not defined
>>> 
>>> 'C' in s
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    'C' in s
NameError: name 's' is not defined
>>> s = set("FishC")
>>> 'C' in s
True
>>> 
>>> for each in s:
	print(each)

	
s
i
h
C
F
>>> 
>>> set([1,1,2,3,5])
{1, 2, 3, 5}
>>> 
>>> s = [1,1,2,3,5]
>>> len(s) == len(set(s))
False
>>> 
>>> #集合的各种方法
>>> 
>>> 
>>> s.isdisjoin("JAVA")
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    s.isdisjoin("JAVA")
AttributeError: 'list' object has no attribute 'isdisjoin'
>>> s = set([1,2,3])
>>> s.isdisjoin("JAVA")
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    s.isdisjoin("JAVA")
AttributeError: 'set' object has no attribute 'isdisjoin'
>>> s.isdisjoint("JAVA")
True
>>> # 是否没有交集
>>> 
>>> #issubset() 是否是子集
>>> 
>>> s.issubset("123456")
False
>>> s.issubset(set("123456"))
False
>>> s.issubset(set([1,2,3,4]))
True
>>> # issuperset()超级
>>> 
>>> #并集union
>>> 
>>> s.union({4,5,6})
{1, 2, 3, 4, 5, 6}
>>> 
>>> # 交集
>>> s.intersection({1,2,4,5})
{1, 2}
>>> 
>>> #差集
>>> s.difference({2,3,4})
{1}
>>> s <= set([1,2,3,4])
True
>>> 
>>> s | {4,5,6}
{1, 2, 3, 4, 5, 6}
>>> 
>>> s & {1,3,5}
{1, 3}
>>> 
>>> # 运算符表示上述的集合关系
>>> 