order = int(input("Enter order of square matrix: "))
matrix = []

for entries in range(order):
    row = list(map(int, input("Enter ELEMENTS: ").split()))
    matrix.append(row)

for i in range(order):
    print(matrix[i])

def det(matrix, order):
    det1 = matrix[0][0]*(matrix[1][1]*matrix[2][2] - matrix[2][1]*matrix[1][2])
    det2 = matrix[0][1]*(matrix[1][0]*matrix[2][2] - matrix[1][2]*matrix[2][0])
    det3 = matrix[0][2]*(matrix[1][0]*matrix[2][1] - matrix[2][0]*matrix[1][1])
    return det1 - det2 + det3

print(det(matrix, order))