Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """ try-except-else """
' try-except-else '
>>> 
>>> try:
	1 / 0
except:
	print("catch")
else:
	print("not catch")

	
catch
>>> 
>>> try:
	1 / 1
except:
	print("catch")
else:
	print("not catch")

	
1.0
not catch
>>> 
>>> """没有捕获异常 就执行else"""
'没有捕获异常 就执行else'
>>> 
>>> """ try-except-finally"""
' try-except-finally'
>>> 
>>> try:
	1 / 1
except:
	print("catch")
else:
	print("not catch")
finally:
	print("no matter catch or not!")

	
1.0
not catch
no matter catch or not!
>>> 
>>> try:
	f = open("FishC.txt","w")
	f.write("I love python")
except:
	print("error")
finally
SyntaxError: invalid syntax
>>> try:
	f = open("FishC.txt","w")
	f.write("I love python")
except:
	print("error")
finally:
	f.close()

	
13
>>> 
>>> """异常的嵌套"""
'异常的嵌套'
>>> 
>>> try:
	try:
		520 + "FishC"
	except:
		print("内部异常")
except:
	print("外部异常")
finally:
	print("收尾")

	
内部异常
收尾
>>> 
>>> try:
	try:
		520 + "FishC"
	except:
		print("内部异常")
	1 / 0
except:
	print("外部异常")
finally:
	print("收尾")

	
内部异常
外部异常
收尾
>>> 
>>> """ raise语句"""
' raise语句'
>>> raise ValyeError("值不正确")
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    raise ValyeError("值不正确")
NameError: name 'ValyeError' is not defined
>>> 
>>> raise ValueError("zhe kebuxing") from ZeroDivisionError
ZeroDivisionError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    raise ValueError("zhe kebuxing") from ZeroDivisionError
ValueError: zhe kebuxing
>>> 
>>> """assert语句"""
'assert语句'
>>> 
>>> s = "FishC"
>>> assert s == "FishC"
>>> assert s !== "FishC"
SyntaxError: invalid syntax
>>> assert s != "FishC"
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    assert s != "FishC"
AssertionError
>>> """asset 不正确会抛错"""
'asset 不正确会抛错'
>>> 
>>> """利用异常实现goto"""
'利用异常实现goto'
>>> 