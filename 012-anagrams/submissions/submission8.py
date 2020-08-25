import sys

A= sys.argv[1]
B = sys.argv[2]

result_A={}
fake=set(A)
for elem in fake:
    result_A[elem]=A.count(elem)

result_B={}
fake2=set(B)
for elem in fake2:
    result_B[elem]=A.count(elem)


if result_A==result_B:
    print("True")
else:
    print("False")
