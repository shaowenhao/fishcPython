Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """列表，元组，和字符串 """
'列表，元组，和字符串 '
>>> # 1. 都可以通过索引获取每一个元素
>>> # 2. 第一个元素的索引值都是0
>>> # 3. 都可以通过切片的方法获取一个范围
>>> # 4. 都有很多共同的运算符
>>> 
>>> # 统称为序列 根据是否能被修改将序列 分为 可变序列和不可变序列
>>> # 列表是可变序列， 元组和字符串是不可变序列
>>> 
>>> 
>>> """左右序列的一些运算符和函数 """
'左右序列的一些运算符和函数 '
>>> 
>>> 
>>> # 1. + * 号
>>> # 加法表示拼接 * 表示重复
>>> 
>>> [1,2,3] + [4,5,6]
[1, 2, 3, 4, 5, 6]
>>> 
>>> (1,2,3) + (4,5,6)
(1, 2, 3, 4, 5, 6)
>>> 
>>> "abc" + "def"
'abcdef'
>>> 
>>> [1,2,3] * 3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> 
>>> 
>>> 
>>> s = [1,2,3]
>>> id(s)
1763607939968
>>> 
>>> s *= 2
>>> id[s]
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    id[s]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> id(s)
1763607939968
>>> 
>>> # 唯一标识 创建的时候就存在的
>>> # 类型 和 值 这3个是 对象的
>>> 
>>> n = (1,2,3)
>>> id(n)
1763608555264
>>> 
>>> n *= 2
>>> n
(1, 2, 3, 1, 2, 3)
>>> id(n)
1763607380416
>>> 
>>> 
>>> "鱼" in "鱼C"
True
>>> "C" not in "FishC"
False
>>> 
>>> 
>>> x = "123"
>>> y = "123"
>>> x is y
True
>>> 
>>> del x
>>> del y
>>> x
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    x
NameError: name 'x' is not defined
>>> y
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    y
NameError: name 'y' is not defined
>>> x = [1,2,3,4,5]
>>> x[1:4]
[2, 3, 4]
>>> del x[1:4]
>>> x
[1, 5]
>>> 
>>> 
>>> #只用切片操作
>>> y = [1,2,3,4,5]
>>> y[1:4] = []
>>> y
[1, 5]
>>> 
>>> 
>>> x = [1,2,3]
>>> x.clear()
>>> x
[]
>>> 
>>> 
>>> y = [1,2,3]
>>> del y[:]
>>> y
[]
>>> 
>>> """ 序列上 """
' 序列上 '
>>> 