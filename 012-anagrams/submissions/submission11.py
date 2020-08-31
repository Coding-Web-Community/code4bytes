from collections import Counter
import sys


S, T = sys.argv[1:]
print(Counter(S) == Counter(T))
