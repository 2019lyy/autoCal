#测试手写exec执行多行脚本
exec(
	'''if (5 - 3 < 1):
	\n	print(True)
	\nelse:
	\n	print(False)'''
)

input()