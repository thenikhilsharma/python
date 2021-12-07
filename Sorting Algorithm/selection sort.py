L = [2,10,3,9,8]
n = len(L)
for i in range (n):
    k = L[i]
    j = i-1
    while j>=0 and k<L[j]:
        L[j+1] = L[j]
        j = j-1
    else:
        L[j+1] = k
        print("Sorted List:", L)
