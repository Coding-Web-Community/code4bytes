# Written by manish#9999
# 29/01/2020

a = [2, 8]

total = 10

while True:
    next = a[-2] + 4*a[-1]
    if next > 4*10**6: break
    a += [next]
    total += next

print(total)

