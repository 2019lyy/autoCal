#对象json序列换并文件写入，读取
import json
import os

#JSON序列化的读写文件示例
is_write = False

if (is_write):
	dirc_demo = {}
	dirc_demo['text_text'] = '测试文本变量格式化'
	arr_demo = []
	dirc_demo['arr_demo'] = arr_demo
	arr_demo.append('列表中插入数字')
	arr_demo.append('123')
	arr_demo.append(123)
	with open('test7.txt', 'w+', encoding='utf-8') as f:
		f.write(json.dumps(dirc_demo))
else:
	with open('test7.txt', 'r', encoding='utf-8') as f:
		result = json.loads(f.read())
		print(str(result))


#文件夹及文件操作示例
print(os.getcwd())
os.chdir('../')
print(os.getcwd())
print(os.listdir())

input()