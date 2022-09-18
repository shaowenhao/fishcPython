Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """函数1"""
'函数1'
>>> 
>>> #创建和调用函数
>>> 
>>> def myfunc():
	pass

>>> myfunc()
>>> 
>>> 
>>> def myfunc():
	for i in range(3)"
	
SyntaxError: EOL while scanning string literal
>>> def myfunc():
	for i in range(3):
		print("I love python")

		
>>> myfunc()
I love python
I love python
I love python
>>> 
>>> 
>>> #函数的参数
>>> 
>>> m = "abc"
>>> f"def{m}"
'defabc'
>>> 
>>> def myFunc(name):
	for i in range(3):
		print(f"I love {name}")

		
>>> myFunc("shaowenhao")
I love shaowenhao
I love shaowenhao
I love shaowenhao
>>> 
>>> 
>>> 
>>> 
>>> def myFunc(name,times):
	for i in range(times):
		print(f"I love {name}")

		
>>> myFunc("shaowenhao",5)
I love shaowenhao
I love shaowenhao
I love shaowenhao
I love shaowenhao
I love shaowenhao
>>> 
>>> 
>>> #函数的返回值
>>> 
>>> #return
>>> 
>>> def div(x,y):
	z = x / y
	return z

>>> div(4,2)
2.0
>>> 
>>> 
>>> def div(x,y):
	if y == 0:
		return "除数不能为0"
	else:
		z = x / y
	        return z
	
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> 
>>> def div(x,y):
	if y == 0:
		return "除数不能为0"
	else:
	        return x / y

	
>>> div(4,2)
2.0
>>> div(4,0)
'除数不能为0'
>>> 
>>> 