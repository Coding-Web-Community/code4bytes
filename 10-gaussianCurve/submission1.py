#Written by manish#9999

import requests
st = "manish" # the string
url = "http://codingweb.eu-central-1.elasticbeanstalk.com/"+st
data = []
while len(data) < 5000:
    try:
        resp = requests.get(url=url).json()
    except:
        continue
    for k in resp:
        data += [float(k)]

mean = sum(data)/len(data)

print("Mean =", mean)
total = 0
for num in data:
    total += (num - mean)**2

print("SD =",(total/len(data))**0.5)
