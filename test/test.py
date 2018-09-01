#测试time模块
import time

t0 = time.perf_counter()
while (time.perf_counter() - t0 < 1):
	print(time.perf_counter())

input()