# Written by manish#9999
# 02/02/2020

def roman_to_int(roman):
    values = {'M': 1000,
              'D': 500,
              'C': 100,
              'L': 50,
              'X': 10,
              'V': 5,
              'I': 1
              }
    numbers = [values[ch] for ch in roman]
    total = 0
    n2 = 0
    for n1, n2 in zip(numbers, numbers[1:]):
        if n1 >= n2:
            total += n1
        else:
            total -= n1
    return total + n2

with open("roman_numerals.txt", "r") as f:
    data = f.read()
    f.close()

total = 0
for each in data.split(","):
    total += roman_to_int(each)
print(total)
