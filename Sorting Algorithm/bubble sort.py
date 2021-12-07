L = [2,10,3,9,8]
n = len(L)
for i in range (n):
    for j in range(n-i-1):
        if(L[j]>L[j+1]):
            L[j],L[j+1] = L[j+1],L[j]
print('Sorted List ', L)
