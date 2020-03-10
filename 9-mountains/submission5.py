#Written by bork

import matplotlib.pyplot as pyplot

TEST_ARRAY = [7, 6, 8, 5, 7, 4, 6, 5, 5, 6, 4, 5, 5, 6, 6, 7, 5, 8, 6, 7, 7, 6, 6, 5, 5, 6, 4, 5, 3, 6, 2]
REAL_ARRAY = [9, 8, 8, 7, 9, 8, 10, 9, 11, 10, 10, 9, 9, 8, 10, 7, 11, 8, 12, 9, 11, 10, 10, 9, 9, 8, 8, 9, 7, 8, 6]

answer = []

for count, i in enumerate(REAL_ARRAY):
    if count == 0:
        pass
    else: 
        try:
            if REAL_ARRAY[count+1] < i and REAL_ARRAY[count-1] < i:
                answer.append(count)
        except Exception as e:
            pass

def show():
    pyplot.figure(figsize=(20,5))
    pyplot.plot(REAL_ARRAY)
    pyplot.ylabel("Peaks of Mountains")
    for i in answer:
        if i == 0:
            pass
        else:
            pyplot.axvline(x=i, color="r")
    pyplot.show()

show()
