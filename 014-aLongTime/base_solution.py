from datetime import datetime

deltas = []
codes = []



def splitString(s):
        a = line.split(" - ")
        b = a[1].split(" | ")

        return a[0].rstrip(), b[0].rstrip(), b[1].rstrip()

def toUnixTimestamp(s):
    return float(datetime.strptime(s, '%Y-%m-%d %H:%M:%S').strftime('%s'))

f = open("time.log")
lines = f.readlines()

for line in lines:
    t1, t2, code = splitString(line)

    t1 = toUnixTimestamp(t1)
    t2 = toUnixTimestamp(t2)

    delta = t2 - t1

    deltas.append(delta)
    codes.append(code)

deltas, codes = (list(t) for t in zip(*sorted(zip(deltas, codes))))

shortestCode = codes[0]
longestCode = codes[-1]

print("shortest code: ", shortestCode)
print("longest code: ", longestCode)

average = sum(deltas)/len(deltas)
print(average)

closestToAverage = min(deltas, key=lambda x:abs(x-average))
print("code closest to average: ", codes[deltas.index(closestToAverage)])
