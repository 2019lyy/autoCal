#测试变量转Boolean
arr = []
print('第一次')
if (arr):
	print('true')
else:
	print('false')

print('第二次')
arr.append('qaqa')
if (arr):
	print('true')
else:
	print('false')

input()