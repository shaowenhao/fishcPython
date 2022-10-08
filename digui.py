Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """递归"""
'递归'
>>> 
>>> def funC(i):
	if i > 0:
		print("AWBDYL")
		i -= 1
		funC()

		
>>> funC(10)
AWBDYL
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    funC(10)
  File "<pyshell#7>", line 5, in funC
    funC()
TypeError: funC() missing 1 required positional argument: 'i'
>>> def funC(i):
	if i > 0:
		print("AWBDYL")
		i -= 1
		funC(i)

		
>>> funC(5)
AWBDYL
AWBDYL
AWBDYL
AWBDYL
AWBDYL
>>> 
>>> def factIter(n):
	result = 1
	for i in range(1,n):
		result *= i

		
>>> def factIter(n):
	result = 1
	for i in range(1,n):
		result *= i
	return result

>>> factIter(5)
24
>>> def factIter(n):
	result = n
	for i in range(1,n):
		result *= i
	return result

>>> factIter(5)
120
>>> range(1,5)
range(1, 5)
>>> for i in range(1,5)
SyntaxError: invalid syntax
>>> for i in range(1,5):
	print i
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(i)?
>>> for i in range(1,5):
	print(i)

	
1
2
3
4
>>> 
>>> def factRecur(n):
	if n == 1:
		return 1
	else:
		return n * factRecur(n-1)

	
>>> factRecur(5)
120
>>> 
>>> 
>>> 
>>> def fibRecur(n):
	if n == 1 or n == 2:
		return 1
	else:
		return fibRecur(n-1) + fibRecur(n-2)

	
>>> fibRecur(12)
144
>>> 
>>> 