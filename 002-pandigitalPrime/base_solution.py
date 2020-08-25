array = [i for i in reversed(range(1,8))]
numbers = int(''.join(str(e) for e in array))

def isPandigital(n):
	for i in array[:len(str(n))]:
		if(str(i) not in list(str(n))):
			return False	
				
	
	return True

def buildPrimes(n):
	primes = [True]*(n+1)
	p = 2
	while(p*p <= n):
		if(primes[p]):
			for i in range(p*2, n+1, p):
				primes[i] = False
		p += 1

	return primes

primes = buildPrimes(numbers)
for p in reversed(range(len(primes))):
	if(isPandigital(p) == True):
		if(primes[p] == True):
			print(p)
			break
