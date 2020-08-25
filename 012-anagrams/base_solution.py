import sys

def makeWordMakeup(s):
    x = {}
    for char in s:
        try:
            x[char] += 1
        except:
            x[char] = 1

    return x



def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    sm = makeWordMakeup(s)
    st = makeWordMakeup(t)

    for i in sm:
        try:
            if sm[i] != st[i]:
                return False
        except:
            return False

    return True


def main():
    s = sys.argv[1]
    t = sys.argv[2]

    print(isAnagram(s, t))


main()
