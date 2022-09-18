Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """装饰器函数"""
'装饰器函数'
>>> 
>>> # 把一个函数作为参数传递给另一个函数
>>> 
>>> def myfunc():
	print("正在调用myfunc..")

	
>>> def report(func):
	print("start")
	func()
	print("end")

	
>>> report(myfunc)
start
正在调用myfunc..
end
>>> 
>>> 
>>> import time
>>> def time_master(func):
	print("start")
	start = time.time()
	func()
	stop = time.time()
	print("stop")
	print(f"一共花费了{(stop-start):.2f}秒90")

	
>>> def myfunc():
	time.sleep(2)
	print("Hello wenhao")

	
>>> time_master(myfunc)
start
Hello wenhao
stop
一共花费了2.04秒90
>>> 
>>> 
>>> 