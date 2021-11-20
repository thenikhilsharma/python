n1 = int(input())
A = []
B = []
C = []

for i in range(n1):
    a = int(input())
    A.append(a)

n2 = int(input())

for j in range(n2):
    b = int(input())
    B.append(b)

A.sort()
B.sort()

for x in range(n1):
    if int(A[x]) > int(B[x]):
        C.append(int(A[x]-B[x]))
    else:
        C.append(int(B[x]-A[x]))

Sum = sum(C)
print(Sum)