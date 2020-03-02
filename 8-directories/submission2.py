import os
import hashlib
os.chdir("dir")
startDir = os.getcwd()
def getStrings(directory):
    if "." in directory:
        with open(directory) as text:
            return text.read()
    else:
        addingVar = ""
        for x in sorted(os.listdir(directory)):
            addingVar += str(getStrings(str(directory) + "/" + str(x)))
        return addingVar
hashing = hashlib.sha256()
hashing.update(getStrings(os.getcwd()).encode("utf-8"))
print(hashing.hexdigest())
