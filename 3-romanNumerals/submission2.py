# Written by frog#7088
# 02/02/2020

import csv
romanNumerals = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000
}
romanNumeralsData= [row for row in csv.reader(open("roman_numerals.txt", newline=""))][0]

def parseRomanNumerals(string):
    string = list(string)
    for x in range(len(string)):
        string[x] = romanNumerals[string[x]]
    addingNumber = 0
    for x in range(len(string)):
        try:
            if string[x+1] > string[x]:
                addingNumber += -string[x]
            else:
                addingNumber += string[x]
        except:
            addingNumber += string[x]
    return addingNumber
adding = 0
for x in romanNumeralsData:
    adding += parseRomanNumerals(x)
print(adding)
