import os

base_path = os.path.join(os.getcwd(), "dir")

def scan(path):
	for thing in sorted(os.listdir(path)):
		thing_path = os.path.join(path, thing)
		if(thing[-4:] != ".txt"):
			s = scan(thing_path)
		else:
			s += open(thing_path, "r").read()
	
	return s

import hashlib
print(hashlib.sha256(scan(base_path).encode()).hexdigest())
