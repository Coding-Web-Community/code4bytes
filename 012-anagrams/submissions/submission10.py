import sys

golang = sys.argv[1]
sucks = sys.argv[2]

def kek(golang, sucks):
    liste1 = list(golang)
    liste1.sort()
    liste2 = list(sucks)
    liste2.sort()
    print(liste1 == liste2)

kek(golang, sucks)
