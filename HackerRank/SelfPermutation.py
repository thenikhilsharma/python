A = input()
B = input()

A = list(A)
B = list(B)

A.sort()
B.sort()

if A == B:
    print("1")
else:
    print("0")