import time

def time_master(func):
    def call_func():
        print("start")
        start = time.time()
        func()
        stop = time.time()
        print("stop")
        print(f"spend time {(stop-start):.2f} sec")
    return call_func

@time_master
def myfunc():
    time.sleep(2)
    print("hello world")

myfunc()

# 装饰器函数 语法糖 myfunc = time_master(myfunc) myfunc()


# 多个装饰器再同一个函数上
