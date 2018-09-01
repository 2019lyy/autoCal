#测试字典内容转Boolean
dirc = {}

print(dirc.get(1))
print(dirc.get(1) == None)

dirc[1] = []

print(dirc.get(1))
print(dirc.get(1) == None)

input()