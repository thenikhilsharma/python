no = int(input())
matrix = []

for x in range(no):
    row = list(map(int, input().split()))
    matrix.append(row)

primaryDiagonal = 0
secondaryDiagonal = 0

for i in range (len(matrix)):
    for j in range(len(matrix[i])):
        if i == j:
            primaryDiagonal = primaryDiagonal+matrix[i][j]

for m in range(len(matrix)):
    for n in range(len(matrix[m])):
        if m+n == (no-1):
            secondaryDiagonal = secondaryDiagonal + matrix[m][n]\

if primaryDiagonal < secondaryDiagonal:
    difference = secondaryDiagonal - primaryDiagonal
else:
    difference = primaryDiagonal - secondaryDiagonal

print(difference)