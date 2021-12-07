#by Nikhil Sharma on 3 Dec
#@7:30pm partially solved

t = int(input())
for z in range(t):
    n,m = input().split()
    n = int(n)
    m = int(m)

    arr= []
    hill = [0,1,0]
    valley = [1,0,1]

    if n>m:
        for j in range(n):
            arr.append("1")
        for i in range(1,m+2,2):
            arr.insert(i,"0")
        arr.insert(0,"0")
        arr.insert(m+n+1,"0")
    elif m>n:
        for j in range(m):
            arr.append("0")
        for i in range(1,n+2,2):
            arr.insert(i,"1")
        arr.insert(0,"1")
        arr.insert(m+n+1,"1")
    elif n == m:
        for j in range(n):
            arr.append("1")
        for i in range(1,m+3,2):
            arr.insert(i,"0")
        arr.insert(0,"0")
        arr.insert(m+n+1,"1")

    arr = ''.join(arr)
    print(len(arr))
    print(arr)