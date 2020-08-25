import os
base_path = os.path.join(os.getcwd(), "dir")
def scan(path, s): 
  l = os.listdir(path)
  for thing in sorted(l):
    if("txt" not in str(thing)[-4:]):
      s = scan(os.path.join(path, thing), s)
    else:
      with open(os.path.join(path, thing), "r") as f:
        s += f.read()
        f.close()
  
  return s
s = scan(base_path, "") 
print(len(s))
import hashlib
h = hashlib.sha256(s.encode()).hexdigest()
print(h)
