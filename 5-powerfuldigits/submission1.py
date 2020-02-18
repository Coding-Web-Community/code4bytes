def howMany(length):
    numbers = []
    maxNumber = int("9"*length)**(1/length)
    for x in range(1, int(maxNumber - maxNumber%1 + 1)):
        if len(str(x**length)) == length:
            numbers.append(x)
    print(numbers)
    return len(numbers)
number = 0
for x in range(1,10):
    number += howMany(x)
print(number)
