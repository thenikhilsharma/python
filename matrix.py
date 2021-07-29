def principle_Diagonal(matrix):
    pDiagonal = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j:
                pDiagonal.append(matrix[i][j])
    return pDiagonal

def principle_Diagonal_Sum():
    return sum(principle_Diagonal(matrix))

def order():
    order = int(input("Enter No. of Rows: "))
    return order

matrix = []

size = order()

for column in range (size):
    rows = list(map(int, input().split()))
    matrix.append(rows)

principle_Diagonal(matrix)
print(principle_Diagonal_Sum())

