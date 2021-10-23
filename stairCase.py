n = int(input())

for i in range(n,0,-1):
    if i<n:
        print(end='\n')
    for j in range(1,n+1):
        if j<i:
            print(" ",end="")
        elif j>=i:
            print("*",end="")