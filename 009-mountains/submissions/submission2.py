#written by frog
actual = [9, 8, 8, 7, 9, 8, 10, 9, 11, 10, 10, 9, 9, 8, 10, 7, 11, 8, 12, 9, 11, 10, 10, 9, 9, 8, 8, 9, 7, 8, 6]

end = []
for xi, x in enumerate(actual):
    try:
        if xi != len(actual) and xi != 0 and x > actual[xi-1] and x > actual[xi+1]:
            end.append(xi)
    except:
        pass
print(end)
