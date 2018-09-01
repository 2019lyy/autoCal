#循环调用示例
from threading import Timer

def fun_timer():
    print('Hello Timer!')
    global timer
    timer = Timer(0.5, fun_timer)
    timer.start()

timer = Timer(0.5, fun_timer)
timer.start()