def function(array):
    temp1 = 0
    for xi, x in enumerate(array[:-1]):
        temp2 = array[xi+1] - array[xi]
        if temp1 > temp2:
            return False
        temp1 = temp2
    return True


print(function([1, 3, 7, 15, 27, 44, 63, 86, 107, 134, 168]))
