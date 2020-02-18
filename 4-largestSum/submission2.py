inputArray = [6,1,5,4,2]
addToNumber = 10
output = []
for x in range(len(inputArray)-round((len(inputArray)/2)-((len(inputArray)/2)%1)+1)):
    if inputArray[x] > addToNumber:
        continue
    for y in range(len(inputArray)):
        if x == y:
            continue
            
        if (inputArray[x]+inputArray[y]) == addToNumber:
            output.append(x)
            output.append(y)
print(output)
