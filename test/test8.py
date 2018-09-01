import datetime
import os

nowtime = datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
print(nowtime)



def showDir1():
	print(os.getcwd())

def showDir2():
	os.chdir('../')
	print(os.getcwd())

showDir1()
showDir2()
showDir1()
showDir2()

input()