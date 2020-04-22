import numpy as np

test = [1, 3, 7, 15, 27, 44, 63, 86, 107, 134, 168]

prev = test[1] - test[0]
print(prev)
for i in range(2, len(test)):
	cur = test[i] - test[i-1]
	print(cur)
	if cur < prev:
		print("no")
		break
	else:
		prev = cur
		print("yes")

print(np.gradient(np.gradient([2, 4, 7, 13])))

print(np.gradient(np.gradient([3, 10, 15, 21])))
