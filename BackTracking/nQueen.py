def isSafe(arr, x, y, n):

    for row in range(0, x, 1):
        if arr[row][y] == 1:
            return False
    
    row = x
    col = y

    while row >= 0 and col >= 0:
        if arr[row][col] == 1:
            return False
        row -= 1
        col -= 1
    
    row = x
    col = y

    while row >= 0 and col < 0:
        if arr[row][col] == 1:
            return False
        row -= 1
        col += 1
    
    return True

def nQueen(arr, x, n):

    if (x >= n):
        return True
    
    for col in range(0, n, 1):
        if isSafe(arr, x, col, n):
            arr[x][col] = 1
        
            if nQueen(arr, x+1, n):
                return True
        
            arr[x][col] = 0
    
    return False

n = int(input("Input order: "))
arr = []

for l in range(n):
    arr.append([])
    for m in range(n):
        arr[l].append(0)

for i in range(0, n, 1):
    for j in range(0, n, 1):
        arr.append(0)
        arr[i][j] = 0

if nQueen(arr, 0, n):
    for i in range(0, n, 1):
        for j in range(0, n, 1):
            if j != n-1:
                print(arr[i][j], ' ', sep='', end="")
            else:
                print(arr[i][j])