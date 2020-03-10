#written by frog
actual = [9, 8, 8, 7, 9, 8, 10, 9, 11, 10, 10, 9, 9, 8, 10, 7, 11, 8, 12, 9, 11, 10, 10, 9, 9, 8, 8, 9, 7, 8, 6]

# Example:
example = [7, 6, 8, 5, 7, 4, 6, 5, 5, 6, 4, 5, 5, 6, 6, 7, 5, 8, 6, 7, 7, 6, 6, 5, 5, 6, 4, 5, 3, 6, 2] 
# Solution:
# [2, 4, 6, 9, 15, 17, 25, 27, 29] 
end = []
for xi, x in enumerate(actual):
    try:
        if xi != len(actual) and xi != 0 and x > actual[xi-1] and x > actual[xi+1]:
            end.append(xi)
    except:
        pass
print(end
)
