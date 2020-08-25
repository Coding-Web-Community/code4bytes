import random
import os
import string

def getRandomName():
	return ''.join(random.choice(string.ascii_lowercase) for _ in range(10))

def createFile(path):
	with open(os.path.join(path, getRandomName() + ".txt"), "w") as file:
		file.write(getRandomName())
		file.close()

def createDir(path):
	dir_name = os.path.join(path, getRandomName())
	os.mkdir(dir_name)
	
	return dir_name

def enterloop(path, depth):
	if depth > 0:
		temp_paths = []
		for i in range(random.randint(1,10)):
			print(i)
			temp_paths.append(createDir(path))

		for temp_path in temp_paths:
			enterloop(temp_path, depth - 1)
	else:
		createFile(path)

start_path = os.path.join(os.getcwd(), "dir")

enterloop(start_path, 5)
		
	
