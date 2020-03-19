import requests
import matplotlib.pyplot as plt
from tqdm import tqdm
import numpy as np
import time

url = "http://codingweb.eu-central-1.elasticbeanstalk.com/golang"
a = []

start = time.time()

while len(a) < 100000:
	print(len(a))
	r = requests.get(url=url)
	if("429" in str(r)):
		print("sleeping")
		time.sleep(.1)
	else:
		data = r.json()
		#print(data)
		for d in data:
			a.append(float(d))
	
	#time.sleep(1)

print(time.time() - start)

plt.hist(a, 20)
plt.show()

mean = sum(a)/len(a)

t = 0
for num in a:
	t += (num - mean)**2
	
std = np.sqrt((1/len(a))*t)

print(mean, std)
