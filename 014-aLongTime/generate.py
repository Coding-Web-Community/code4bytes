import random
from datetime import datetime
import string
from tqdm import tqdm

LEN = 1700000
MAX = 1600612413

file = open("time.log", "a+")


def randomString():
    return ''.join(random.choice(string.ascii_letters) for i in range(10))


def toFormatted(smallest, biggest):
    dtf = '%Y-%m-%d %H:%M:%S'
    smallest = datetime.utcfromtimestamp(smallest).strftime(dtf)
    biggest = datetime.utcfromtimestamp(biggest).strftime(dtf)

    return "{} - {} | {}\n".format(smallest, biggest, randomString())

for _ in tqdm(range(round(LEN/2))):

    d1 = random.randrange(MAX)
    d2 = random.randrange(MAX)

    if d1 < d2:
        f = toFormatted(d1, d2)
    else:
        f = toFormatted(d2, d1)

    file.write(f)

file.close()
