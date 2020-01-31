# Written by frog#7088
# 30/01/2020
def pandig(number):
    number = str(number)
    numbers = {}
    for x in number:
        if x in numbers:
            return(False)
        elif int(x) > len(number):
            return(False)
        numbers[x] = None
    return(True)
def isPrime(number):
    numberMax = round(number**0.5)+1
    for x in range(2, numberMax):
        if not number % x:
            return False
    return True
def genPrimes(maxNumber):
    maxPrimeNumber = round(maxNumber**0.5)+1
    badIndex = []
    forLoopArray = list(range(2,maxPrimeNumber))
    print(forLoopArray)
    for x in forLoopArray:
        if isPrime(x):
            print(x)
            currentNumber = x
            while True:
                currentNumber += x
                if currentNumber >= maxNumber:
                    break
                if not currentNumber in badIndex:
                    badIndex.append(currentNumber)
    finalList = list(set(range(1,maxNumber+1))-set(badIndex))
    finalList.pop(-1)
    finalList.pop(0)
    return(finalList)
largest = 0
primeList = genPrimes(7654321)
for x in primeList:
    if pandig(x):
        largest = x
print(largest)
