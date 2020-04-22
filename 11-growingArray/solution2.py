lst1 = [1, 3, 7, 15, 27, 44, 63, 86, 107, 134, 168]


def is_strictly_positive(lst):
    previous_value = 0
    for index in range(1, len(lst)-1):
        gradient = lst[index] - lst[index-1]
        if gradient < previous_value:
            return False
        previous_value = gradient

    return True


print(is_strictly_positive(lst1))
