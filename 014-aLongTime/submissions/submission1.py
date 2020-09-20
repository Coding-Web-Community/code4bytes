import datetime
import json
array = []
with open('time.log') as timelog:
    for row in timelog:
        a = row.split(' | ')
        t = a[0].split(' - ')
        array.append(((datetime.datetime.fromisoformat(t[1]) - datetime.datetime.fromisoformat(t[0])).total_seconds(), a[1]))
array.sort()
print("shortest time delta:",min(array, key = lambda x: x[0])[1][:-1])
print("longest time delta:", max(array, key = lambda x: x[0])[1][:-1])

avg = sum(map(lambda x: x[0],array))/len(array)
print(avg)
print("code closest to average time delta:", min(array, key = lambda x: abs(x[0] - avg))[1][:-1])
