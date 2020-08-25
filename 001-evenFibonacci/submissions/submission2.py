# Written by frog#7088
# 01/29/2020


# First implementation

cache = {}
def evenFib(number):
    if number in cache:
        return(cache[number])
    else:
        if number == 0:
            return(0)
        elif number == 1:
            return(2)
        else:
            cacheAdd = (4 * evenFib(number-1)) + evenFib(number-2)
            cache[number] = cacheAdd
            return(cacheAdd)

milEvenFibs = 0
x = 1
while True:
    temp = evenFib(x)
    x += 1
    if temp > 4_000_000:
        break
    milEvenFibs += temp
print(milEvenFibs)

# Second Implementation

cache = [0,2]
milEvenFibs = 0
cacheAdd = 2
while True:
    milEvenFibs += cacheAdd
    cacheAdd = (4 * cache[1]) + cache[0]
    cache[0] = cache[1]
    cache[1] = cacheAdd
    if cacheAdd > 4_000_000:
        break
print(milEvenFibs)

