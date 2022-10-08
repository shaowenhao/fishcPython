Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """ with语句和上下文管理器"""
' with语句和上下文管理器'
>>> 
>>> f = open("FishC.txt","w")
>>> f.write("I love python")
13
>>> f.close()
>>> 
>>> with open("FishC.txt","w") as f:
	f.write("I love python......")

	
19
>>> """不需要手动关闭"""
'不需要手动关闭'
>>> """确保资源的释放"""
'确保资源的释放'
>>> 
>>> 
>>> with open("FishC.txt","w") as f:
	f.write("I love python......")
	1 / 0

	
19
Traceback (most recent call last):
  File "<pyshell#15>", line 3, in <module>
    1 / 0
ZeroDivisionError: division by zero
>>> """即使有错 也会关闭"""
'即使有错 也会关闭'
>>> 
>>> """ pickle  序列化第一人"""
' pickle  序列化第一人'
>>> 
===================== RESTART: D:\dev_tool\Python\write.py =====================
>>> 
====================== RESTART: D:\dev_tool\Python\read.py =====================
1
2
3
FishC
['小甲鱼', 520, 3.14]
{'one': 1, 'two': 2}
>>> 