from os import getcwd, listdir
from os.path import isfile, join
dir = "C:/Users/mmk/Downloads/dir"
class F:
    t=None
def travel(dir):
    print(dir)
    for dirs in listdir(dir):
        if not isfile(join(dir, dirs)):
            travel(join(dir, dirs))
        else:
            with open(join(dir, dirs), "rb") as f:
                data = f.read()
                if not F.t:F.t=data
                else: F.t += data
                f.close()
travel(dir)
print(F.t)
from hashlib import sha256
print(sha256(F.t).hexdigest())
