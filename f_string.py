Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """F string"""
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
>>> 