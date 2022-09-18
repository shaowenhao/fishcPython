Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> >>> """F string"""
'F string'
>>> 
>>> "鱼C工作室成立于"
'鱼C工作室成立于'
>>> 
>>> year = 2020
>>> 
>>> F"鱼C工作室成立于{year}"
'鱼C工作室成立于2020'
>>> 
>>> 
>>> f"2的平方是{2*2}"
'2的平方是4'
>>> 
>>> f{"-520:010"}
SyntaxError: invalid syntax
>>> f"{-520:010}"
'-000000520'
>>> 
>>> f"{3.1415:.2f}"
'3.14'
>>> 
>>> "{:+} {:-}".format(520,-520)
SyntaxError: invalid syntax
>>> "{:,}".format(1234)
'1,234'
>>> 
>>> # 对于[type]设置为f或F的浮点数来说 限定小数点后显示多少位
>>> #对于 设置为g或者G的浮点数，限定小数点前后一共显示多少位
>>> # 对非数字类型来说，限定的是最大字段的代销
>>> 
>>> {:.2g}.format(3.1215)
SyntaxError: invalid syntax
>>> "{:.2g}".format(3.1215)
'3.1'
>>> 
>>> 
>>> "{:.6}".format("I love FishC")
'I love'
>>> 
>>> 