#By Nikhil Sharma on 20 dec 2021
#@ 1:42 am

for _ in range(int(input())):
    n = int(input())
    matrix = []
    for inp in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    #
    def trace(i, j):
        ans = 0
        if i == n and j == n:
            return ans
        else:
            ans += matrix[i][j]
        if i+1 in range(n) and j+1 in range(n):
            return ans + trace(i+1, j+1)
        else:
            return ans
    
    ans = 0
    for i in range(n):
        for j in range(n):
            result = trace(i, j)
            ans = result if result > ans else ans
    print(ans)