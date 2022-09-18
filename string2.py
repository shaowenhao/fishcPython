Python 3.8.9 (tags/v3.8.9:a743f81, Apr  6 2021, 14:02:34) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> >>> x = "12321"
>>> 
>>> "是回文数" if x == x[::-1] else "不是回文数"
'是回文数'
>>> 
>>> 
>>> #大小写字母
>>> """
capitalize()  casefold() title() swapcase() upper() lowe() """
'\ncapitalize()  casefold() title() swapcase() upper() lowe() '
SyntaxError: invalid syntax
>>> 
>>> str = "Hello, Shao Wenhao"
>>> 
>>> str.capotalize()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    str.capotalize()
AttributeError: 'str' object has no attribute 'capotalize'
>>> str.capitalize()
'Hello, shao wenhao'
>>> 
>>> str.casefold()
'hello, shao wenhao'
>>> 
>>> str.title()
'Hello, Shao Wenhao'
>>> 
>>> str.swapcase()
'hELLO, sHAO wENHAO'
>>> 
>>> str.uper()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    str.uper()
AttributeError: 'str' object has no attribute 'uper'
>>> str.upper()
'HELLO, SHAO WENHAO'
>>> 
>>> str.lowe()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    str.lowe()
AttributeError: 'str' object has no attribute 'lowe'
>>> str.lower()
'hello, shao wenhao'
>>> 
>>> #左中右对齐
>>> """ center(width,fillchar='') rjust(width,fillchar='' zfill(width) ljust(width,fillchar=''))
"""
" center(width,fillchar='') rjust(width,fillchar='' zfill(width) ljust(width,fillchar=''))\n"
>>> 
>>> x = "有内鬼，停止交易！"
>>> x.center(5)
'有内鬼，停止交易！'
>>> x.center(15)
'   有内鬼，停止交易！   '
>>> x.ljust(15)
'有内鬼，停止交易！      '
>>> 
>>> x.rjust(15)
'      有内鬼，停止交易！'
>>> 
>>> x.zfill(15)
'000000有内鬼，停止交易！'
>>> x.center(15,"啊")
'啊啊啊有内鬼，停止交易！啊啊啊'
>>> x.ljust(15,"哦")
'有内鬼，停止交易！哦哦哦哦哦哦'
>>> 
>>> 
>>> 
>>> #查找
>>> """count(sub[,start[,end]]) find(sub[,start[,end]]) rfind(sub[,start[,end]]) index(sub[,start[,end]]) rindex(sub[,satrt[,end]])"""
'count(sub[,start[,end]]) find(sub[,start[,end]]) rfind(sub[,start[,end]]) index(sub[,start[,end]]) rindex(sub[,satrt[,end]])'
>>> 
>>> 
>>> x = "上海自来水来自海上"
>>> 
>>> x.count("海")
2
>>> 
>>> x.count("海",0,5)
1
>>> 
>>> x.find("海")
1
>>> 
>>> x.rfind("海")
7
>>> 
>>> x.find("娃")
-1
>>> 
>>> x.index("娃")
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    x.index("娃")
ValueError: substring not found
>>> 
>>> 
>>> 
>>> #替换
>>> 
>>> """ expandtabs([tabsize=8]) replace(old,new,count=-1) translate(table)
"""
' expandtabs([tabsize=8]) replace(old,new,count=-1) translate(table)\n'
>>> 
>>>  code="""
SyntaxError: unexpected indent
>>> code = """
	print("a b c")
    print("d e f")
"""
>>> new_code = code.expandtabs(4)
>>> new_code
'\n    print("a b c")\n    print("d e f")\n'
>>> print(new_code)

    print("a b c")
    print("d e f")

>>> "hello world".replace("o","O")
'hellO wOrld'
>>> 
>>> 
>>> table = str.maketrans('ABCDEFG','1234567')
>>> 'I love FishC'.translate(table)
'I love 6ish3'
>>> 
>>> 
>>> #判断
>>> 
>>> #isXXXX() startswith endswith
>>> 
>>> x = "我爱Python"
>>> x.startswith("我")
True
>>> 
>>> x.endswith("Python")
True
>>> x.startswith("爱",1)
True
>>> x.endswith("Py",0,4)
True
>>> 
>>> 
>>> x = "她爱Pyhon"
>>> if x.startswith(("你","我","她")):
	
	print("总有人爱Pyhon")

	
总有人爱Pyhon
>>> #元组中有一个匹配的
>>> 
>>> x =  "I love Python"
>>> x.istitle()
False
>>> x.isupper()
False
>>> 
>>> x.isalpha()
False
>>> "IlovePython".isalpha()
True
>>> 
>>> x = 12345
>>> x.isdecimal()
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    x.isdecimal()
AttributeError: 'int' object has no attribute 'isdecimal'
>>> x = "12345"
>>> x.isdecimal()
True
>>> x.isdigit()
True
>>> 
>>> x.isnumeric()
True
>>> "I am a good gay".isidentifier()
False
>>> "I_am_a_good_gay".isidentifier()
True
>>> 
>>> import keyword
>>> keyword.iskeyword("if")
True
>>> 
>>> keyword.iskeyword("py")
False
>>> 
>>> 
>>> #引入keword库 验证是否是pyhon保留关键字
>>> 
>>> #截取
>>> """ strip(chars=None) lstrip(chars=None) rstrip removeprefix(prefix) removesuffix(suffix)
"""
' strip(chars=None) lstrip(chars=None) rstrip removeprefix(prefix) removesuffix(suffix)\n'
>>> 
>>> "    左侧不要留白".lstrip()
'左侧不要留白'
>>> 
>>> "右侧不要留白    ".rstrip()
'右侧不要留白'
>>> 
>>> "www.ilovefishc.com".lstrip("wcom.")
'ilovefishc.com'
>>> "www.ilovefishc.com".rstrip("wcom.")
'www.ilovefish'
>>> 
>>> "www.ilovefishc.com".strip("wcom.")
'ilovefish'
>>> 
>>> #括号里的字符串再匹配的时候是单个逐一匹配的
>>> 
>>> "www.ilovefishc.com".removeprefix("www.")
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    "www.ilovefishc.com".removeprefix("www.")
AttributeError: 'str' object has no attribute 'removeprefix'
>>> 
>>> 
>>> #当前yhonh是3.8.9 该函数式3.9+才有
>>> 
>>> 
>>> #拆分 & 拼接
>>> 
>>> """ partition(sep)  rpartition()sep """
' partition(sep)  rpartition()sep '
>>> 
>>> "www.ilovefishc.com".partition(".")
('www', '.', 'ilovefishc.com')
>>> # 一个三元组 左边部分 分隔符 右边部分
>>> 
>>> 
>>> "www.ilovefishc.com".rpartition(".")
('www.ilovefishc', '.', 'com')
>>> 
>>> 
