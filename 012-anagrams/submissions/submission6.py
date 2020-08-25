import sys

if __name__ == "__main__":
    sys.argv = sys.argv[1:]
    w1 = sys.argv[0]
    w2 = sys.argv[1]
    print(True if sorted(list(w1)) == sorted(list(w2)) else False)
