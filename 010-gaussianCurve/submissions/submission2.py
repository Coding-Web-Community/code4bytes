#Written by Blackware

import requests
import time
import json
import statistics


print("Key: blackware")

finalList = []

for alz in range(100):
    response = requests.get("http://codingweb.eu-central-1.elasticbeanstalk.com/blackware")
    if(response.status_code == 200):
        print("Successful call: " + str(response.status_code))
        lijst = response.json()
        # using naive method to perform conversion 
        for i in range(0, len(lijst)): 
            lijst[i] = float(lijst[i]) 

        finalList.append(lijst)
        print("SAMPLE: " + str(alz))
        time.sleep(2.5)

x = statistics.mean(lijst)
print("MEAN: " + str(x))

a = statistics.stdev(lijst)
print("STDEV: " + str(a))    
