Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> "苟日新，日日新，又日新".split(",",1)
['苟日新，日日新，又日新']
>>> 
>>> "苟日新，日日新，又日新".split(',',1)
['苟日新，日日新，又日新']
>>> 
>>> "苟日新，日日新，又日新".rsplit(',',1)
['苟日新，日日新，又日新']
>>> "苟日新，日日新，又日新".rsplit(', ',1)
['苟日新，日日新，又日新']
>>> 
================================ RESTART: Shell ================================
>>> "你好,我好,大家好".split(',',1)
['你好', '我好,大家好']
>>> 
>>> "你好,我好,大家好".rsplit(',',1)
['你好,我好', '大家好']
>>> 
>>> "你好\n,我好\n,大家好\r\n".rsplitlines()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    "你好\n,我好\n,大家好\r\n".rsplitlines()
AttributeError: 'str' object has no attribute 'rsplitlines'
>>> "你好\n,我好\n,大家好\r\n".splitlines()
['你好', ',我好', ',大家好']
>>> 
>>> #按换行符切割
>>> 
>>> "你好\n,我好\n,大家好\r\n".splitlines(True)
['你好\n', ',我好\n', ',大家好\r\n']
>>> 
>>> 
>>> #拼接
>>> ".".join("www","baidu","com")
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    ".".join("www","baidu","com")
TypeError: str.join() takes exactly one argument (3 given)
>>> ".".join(["www","baidu","com"])
'www.baidu.com'
>>> 
>>> 
>>> #join里面用列表或元组都可以
>>> ".".join(("www","baidu","com"))
'www.baidu.com'
>>> 
>>> 
>>> s =  "FishC"
>>> s += s
>>> s
'FishCFishC'
>>> 
>>> "".join(("FishC","FishC"))
'FishCFishC'
>>> 