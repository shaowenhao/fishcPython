Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """永久存储"""
'永久存储'
>>> f = open("FishC.txt","w")
>>> 
>>> f.write("I love python.")
14
>>> 
>>> f.writelines(["I love FishC,\n","I love my wife."])
>>> 
>>> f.close()
>>> 
>>> """重新打开"""
'重新打开'
>>> 
>>> f = open("FishC.txt","r+")
>>> 
>>> f.readable()
True
>>> 
>>> f.writeable()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    f.writeable()
AttributeError: '_io.TextIOWrapper' object has no attribute 'writeable'
>>> f.writable()
True
>>> for each in f:
	print(each)

	
I love python.I love FishC,

I love my wife.
>>> 
>>> f.tell()
44
>>> """返回当前文件指针再文件对象中的位置"""
'返回当前文件指针再文件对象中的位置'
>>> f.seek(0)
0
>>> 
>>> f.readline()
'I love python.I love FishC,\n'
>>> f.tell()
29
>>> f.read()
'I love my wife.'
>>> 
>>> f.write("I love my WIFI.")
15
>>> f.fluh()
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    f.fluh()
AttributeError: '_io.TextIOWrapper' object has no attribute 'fluh'
>>> f.flush()
>>> 