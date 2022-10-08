Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """异常"""
'异常'
>>> try:
	1 / 0
except:
	print("error")

	
error
>>> try:
	1 / 0
except ZeroDivisionError as e:
	print(e)

	
division by zero
>>> 1 / 0
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    1 / 0
ZeroDivisionError: division by zero
>>> 
>>> try:
	1 / 0
	520 +"FishC"
except(ZeroDivisionError,valueError,TypeError):
	pass

Traceback (most recent call last):
  File "<pyshell#18>", line 2, in <module>
    1 / 0
ZeroDivisionError: division by zero

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#18>", line 4, in <module>
    except(ZeroDivisionError,valueError,TypeError):
NameError: name 'valueError' is not defined
>>> try:
	1 / 0
	520 +"FishC"
except(ZeroDivisionError,ValueError,TypeError):
	pass

>>> 
>>> 
>>> 
>>> try:
	1 / 0
	520 +"FishC"
except ZeroDivisionError:
	print("除数不能为0")
except ValueError:
	print("值不正确")
except TypeError:
	print（"类型不正确"）
	
SyntaxError: invalid character '（' (U+FF08)
>>> try:
	1 / 0
	520 +"FishC"
except ZeroDivisionError:
	print("除数不能为0")
except ValueError:
	print("值不正确")
except TypeError:
	print("类型不正确"）
	      
SyntaxError: invalid character '）' (U+FF09)
>>> try:
	1 / 0
	520 +"FishC"
except ZeroDivisionError:
	print("除数不能为0")
except ValueError:
	print("值不正确")
except TypeError:
	print("类型不正确")

	
除数不能为0
>>> 