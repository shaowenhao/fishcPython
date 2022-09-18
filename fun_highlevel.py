import time

def logger(msg):
    def time_master(func):
        def call_func():
            start = time.time()
            func()
            stop = time.time()
            print(f"{msg} 耗费了 {(stop-start):.2f}")
        return call_func
    return time_master

@logger(msg="A")
def funA():
    time.sleep(2);
    print("now invoke funA")

funA()


# funA = logger(msg = "A")(funA)

