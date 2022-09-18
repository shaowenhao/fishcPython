Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """字典"""
'字典'
>>> 
>>> x = {"吕布","关羽"}
>>> 
>>> type(x)
<class 'set'>
>>> 
>>> y = {"吕布":"口口布"，"关羽":"关羽羽"}
SyntaxError: invalid character '，' (U+FF0C)
>>> y = {"吕布":"口口布","关羽":"关羽羽"}
>>> type(y)
<class 'dict'>
>>> 
>>> y{"吕布"}
SyntaxError: invalid syntax
>>> y["吕布"]
'口口布'
>>> 
>>> 
>>> y["刘备"] = "刘Baby"
>>> 
>>> y
{'吕布': '口口布', '关羽': '关羽羽', '刘备': '刘Baby'}
>>> 
>>> #创建字典的几种方式
>>> 
>>> a = {"吕布":"口口布","关羽":"关羽羽"}
>>> b = dict(吕布="口口布",关羽="关羽羽")
>>> c = dict([("吕布","口口布"),（"关羽":"关羽羽"）])
SyntaxError: invalid character '（' (U+FF08)
>>> c = dict([("吕布","口口布"),（"关羽","关羽羽"）])
SyntaxError: invalid character '（' (U+FF08)
>>> c = dict([("吕布","口口布"),（"关羽","关羽羽")])
SyntaxError: invalid character '（' (U+FF08)
>>> 
>>> c = dict([("吕布", "口口布"),（"关羽", "关羽羽")])
SyntaxError: invalid character '（' (U+FF08)
>>> c = dict([("吕布", "口口布"),("关羽", "关羽羽")])
>>> 
>>> d =dict({"吕布":"口口布","关羽":"关羽羽"})
>>> 
>>> e = dict({"吕布":"口口布","关羽":"关羽羽"},刘备="刘Baby")
>>> 
>>> f = dict(zip(["吕布","关羽"],["口口布","关羽羽"]))
>>> 
>>> a == e == b == c == f
False
>>> # 如果都是3个 就是True
>>> 
>>> 
>>> # 增
>>> 
>>> d = dict.fromkeys("Fish",20)
>>> d
{'F': 20, 'i': 20, 's': 20, 'h': 20}
>>> 
>>> d['F'] = 200
>>> 
>>> d
{'F': 200, 'i': 20, 's': 20, 'h': 20}
>>> 
>>> d['C'] = 67
>>> 
>>> d
{'F': 200, 'i': 20, 's': 20, 'h': 20, 'C': 67}
>>> 
>>> d.pop('s')
20
>>> d
{'F': 200, 'i': 20, 'h': 20, 'C': 67}
>>> d.pop("狗","没有")
'没有'
>>> 
>>> d.popitem()
('C', 67)
>>> #3.7版本后 字典有序的 popitem 弹出最后加到字典的键值对
>>> 
>>> del d['i']
>>> d
{'F': 200, 'h': 20}
>>> 
>>> 
>>> d = dict.fromkeys("FishC","100")
>>> d
{'F': '100', 'i': '100', 's': '100', 'h': '100', 'C': '100'}
>>> d.clear()
>>> d
{}
>>> 