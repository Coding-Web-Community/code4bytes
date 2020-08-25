import random
import matplotlib.pyplot as plt


def makeMountain(length):
	array = [random.randrange(0,20)]
	for i in range(length):
		if random.randrange(0,2) == 1 :
			array.append(array[i-1]+1)
		else:
			array.append(array[i-1]-1)
	return array
	

def findMountainTops(array):
	maxi = []
	
	for i in range(1,len(array)-1):
		if(array[i-1] < array[i] and array[i+1] < array[i]):
			maxi.append(i)
	
	return maxi

array = makeMountain(30)
plt.plot(array)
mtntops = findMountainTops(array)
for i in range(len(mtntops)):
	plt.axvline(mtntops[i], 0, 1)

print(array)
print(mtntops)
plt.show()
