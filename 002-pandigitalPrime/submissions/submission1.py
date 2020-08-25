# Written by manish#9999
# 30/01/2020

def get_primes(n):
  m = n+1
  numbers = [True] * m
  for i in range(2, int(n**0.5 + 1)):
    if numbers[i]:
      for j in range(i*i, m, i):
        numbers[j] = False
  primes = []
  for i in range(2, m):
    if numbers[i]:
      primes.append(i)
  return primes

primes = get_primes(9999999)
answer = 0
for each in primes:
    if sorted([int(k) for k in str(each)]) == [i+1 for i in range(len(str(each)))]:
        answer = each
print(answer)
