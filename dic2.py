Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """"""
''
>>> d = dict.fromkeys("FishC")
>>> 
>>> d
{'F': None, 'i': None, 's': None, 'h': None, 'C': None}
>>> 
>>> d['s'] = 115
>>> d
{'F': None, 'i': None, 's': 115, 'h': None, 'C': None}
>>> 
>>> d.update({'i':105,'h':104})
>>> d
{'F': None, 'i': 105, 's': 115, 'h': 104, 'C': None}
>>> d.update(F='70',C='67')
>>> 
>>> 



>>> #查
>>> d['C']
'67'
>>> 
>>> d['c']
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    d['c']
KeyError: 'c'
>>> 
>>> d.get('c',"no c here")
'no c here'
>>> 
>>> 
>>> #items() keys() values()
>>> 
>>> d
{'F': '70', 'i': 105, 's': 115, 'h': 104, 'C': '67'}
>>> 
>>> d.setdefault('c',"code")
'code'
>>> d
{'F': '70', 'i': 105, 's': 115, 'h': 104, 'C': '67', 'c': 'code'}
>>> 
>>> keys = d.keys()
>>> values = d.values()
>>> 
>>> keys
dict_keys(['F', 'i', 's', 'h', 'C', 'c'])
>>> 
>>> values
dict_values(['70', 105, 115, 104, '67', 'code'])
>>> 
>>> items = d.items()
>>> 
>>> items
dict_items([('F', '70'), ('i', 105), ('s', 115), ('h', 104), ('C', '67'), ('c', 'code')])
>>> 
>>> 
>>> len(d)
6
>>> 'C' in d
True
>>> list(d)
['F', 'i', 's', 'h', 'C', 'c']
>>> list(d.values())
['70', 105, 115, 104, '67', 'code']
>>> 
>>> 
>>> e = iter(d)
>>> next(e)
'F'
>>> next(e)
'i'
>>> next(e)
's'
>>> next(e)
'h'
>>> next(e)
'C'
>>> next(e)
'c'
>>> next(e)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    next(e)
StopIteration
>>> 
>>> 
>>> list(reversed(d.values()))
['code', '67', 104, 115, 105, '70']
>>> 
>>> 
>>> d = {"吕布":{"语文":60},"关羽":{"语文":80}}
>>> d
{'吕布': {'语文': 60}, '关羽': {'语文': 80}}
>>> 
>>> # 嵌套 某个键的值是字典
>>> d['吕布']
{'语文': 60}
>>> d["吕布"]["语文"]
60
>>> 
>>> d = {"吕布":[60],"关羽":[80]}
>>> d["吕布"][0]
60
>>> 
>>> #字典推导式
>>> 
>>> 
>>> d = {'F':70,'i':105,'s':115,'h':104,'C':67}
>>> b = {v:k for k,v in d.items()}
>>> b
{70: 'F', 105: 'i', 115: 's', 104: 'h', 67: 'C'}
>>> 
>>> 
>>> b = {v:k for k,v in d.items() if v > 100}
>>> b
{105: 'i', 115: 's', 104: 'h'}
>>> 
>>> 
>>> d = {x:ord(x) for x in "FishC"}
>>> d
{'F': 70, 'i': 105, 's': 115, 'h': 104, 'C': 67}
>>> 
>>> 