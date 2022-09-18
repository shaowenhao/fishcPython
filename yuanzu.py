Python 3.8.9 (tags/v3.8.9:a743f81, Apr  6 2021, 14:02:34) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #元组
#列表 [元素1，元素2]
#元组 (元素1，元素2)

>>> 
>>> yz = (1,2,3,4,5,'上单')
>>> yz
(1, 2, 3, 4, 5, '上单')
>>> yz[0]
1
>>> yz[-1]
'上单'
>>> yz[1] = 10
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    yz[1] = 10
TypeError: 'tuple' object does not support item assignment
>>> #元组不可变
>>> 
>>> yz[:3]
(1, 2, 3)
>>> yz[:]
(1, 2, 3, 4, 5, '上单')
>>> 
>>> yz[::2]
(1, 3, 5)
>>> 
>>> yz[::-1]
('上单', 5, 4, 3, 2, 1)
>>> 
>>> nums = (3,1,9,6,8,3,5,3)
>>> nums.count(3)
3
>>> 
>>> heros = ("蜘蛛侠","绿巨人","黑寡妇")
>>> heros.index("黑寡妇")
2
>>> 
>>> s = (1,2,3)
>>> t = (4,5,6)
>>> s + t
(1, 2, 3, 4, 5, 6)
>>> 
>>> s * 3
(1, 2, 3, 1, 2, 3, 1, 2, 3)
>>> w =  s, t
>>> w
((1, 2, 3), (4, 5, 6))
>>> 
>>> 
>>> s = (1,2,3,4,5)
>>> [each * 2 for each in s]
[2, 4, 6, 8, 10]
>>> 
>>> _ = (10,20)
>>> x,y = _
>>> x
10
>>> y
20
>>> 