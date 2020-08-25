nums = [2,3,6,1,5,4,6,9,2,5]
m = 10

d = {}

for i in nums:
	if(i in d):
		print(i)
		print(d[i])
		break
	d[m-i] = i

print(d)
