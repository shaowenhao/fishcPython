Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> s = set("FishC")
>>> s
{'C', 's', 'F', 'i', 'h'}
>>> 
>>> 
>>> #哈希 作用于不可变对象 可变对象不行
>>> 
>>> hash("abc")
3827968589185625928
>>> 
>>> hash((1,2,3))
529344067295497451
>>> 
>>> hash([1,2,3])
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    hash([1,2,3])
TypeError: unhashable type: 'list'
>>> 
>>> hash(s)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    hash(s)
TypeError: unhashable type: 'set'
>>> 