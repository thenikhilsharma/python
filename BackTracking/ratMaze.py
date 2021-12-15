def isSafe(arr, x, y, n):
    if x<n and y<n and arr[x][y] == 1:
        return True
    return False

def ratinMaze(arr, x, y, n, solArr):

    if x == n-1 and y == n-1:
        solArr[x][y] = 1
        return True

    if isSafe(arr, x, y, n):
        solArr[x][y] = 1
        if ratinMaze(arr, x+1, y, n, solArr):
            return True
        
        if ratinMaze(arr, x, y+1, n, solArr):
            return True
        
        solArr[x][y] = 0        #backtracking
        return False
    
    return False

n = int(input("Enter size: "))

arr = []
solArr = []

for i in range(0, n, 1):
    inp = list(map(int, input('Enter row: ').split()))
    arr.append(inp)

for l in range(n):
    solArr.append([])
    for m in range(n):
        solArr[l].append(0)

if ratinMaze(arr, 0, 0, n, solArr):
    for i in range(0, n, 1):
        for j in range(0, n, 1):
            if j != n-1:
                print(solArr[i][j], ' ', sep='', end='')
            else:
                print(solArr[i][j], ' ', sep='')