#测试字符串操作
string = 'list[3][5]'

arr = string.split('[')
del arr[0]
result = []
print(arr)
for entry in arr:
	result.append(entry[0: -1])

print(result)

input()