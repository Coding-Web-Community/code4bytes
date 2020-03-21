#written by frog

import requests
import statistics
import time
number_of_requests = 100
numbers = []
key = 'frogtd'
for _ in range(number_of_requests):
    r = requests.get('http://codingweb.eu-central-1.elasticbeanstalk.com/' + key)
    text = r.text
    text = text[2:-3].split('","')
    numbers += list(map(lambda x: float(x), text))
    time.sleep(0.55)

print("Mean:", statistics.mean(numbers))
print("stdev:", statistics.stdev(numbers))
