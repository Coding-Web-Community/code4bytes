from sys import argv
a = sorted(list(argv[1]))
b = sorted(list(argv[2]))
print((len(a) == len(b)) and (a == b))
