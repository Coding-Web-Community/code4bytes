# Written by Miracul!cKz#6933
# 03/02/2020

romans = []
import csv
with open('roman_numerals.txt', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        romans.append(row)
romans = romans[0]
#print(romans[0][1])
#print(len(romans))
arabec = np.zeros(len(romans))
for i in range(len(romans)):
    for j in range(len(romans[i])):
        if romans[i][j] == "M":
            arabec[i] += 1000 
        elif romans[i][j] == "D":
            arabec[i] += 500 
        elif romans[i][j] == "C":
            arabec[i] += 100
        elif romans[i][j] == "L":
            arabec[i] += 50
        elif romans[i][j] == "X":
            arabec[i] += 10 
        elif romans[i][j] == "V":
            arabec[i] += 5
        elif romans[i][j] == "I":
            arabec[i] += 1 
                  
print(sum(arabec))

