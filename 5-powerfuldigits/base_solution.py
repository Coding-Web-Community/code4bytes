x = []
for n in range(1, 25):
	top = 10**n	
	i = 1	
	while True:
		c = i**n
		if(c > top):
			break
		elif(len(str(c)) == n):
			print(i, n, len(str(c)), c)
			x.append(c)	
		i+=1

print(x)
print(len(x))
