#written by jamie sin

import matplotlib.pyplot as plt
a = [9, 8, 8, 7, 9, 8, 10, 9, 11, 10, 10, 9, 9, 8, 10, 7, 11, 8, 12, 9, 11, 10, 10, 9, 9, 8, 8, 9, 7, 8, 6]
#a = [7, 6, 8, 5, 7, 4, 6, 5, 5, 6, 4, 5, 5, 6, 6, 7, 5, 8, 6, 7, 7, 6, 6, 5, 5, 6, 4, 5, 3, 6, 2] 

i = 1
inds = []
vals = []
while i < len(a) -1:
    if a[i-1] < a[i] and a[i] > a[i+1]:
        inds.append(i)
        vals.append(a[i])
    i += 1
print(inds, vals)
plt.plot(inds, vals)
plt.xlabel('Index Found At')
plt.ylabel('Values at the index')
plt.show()
