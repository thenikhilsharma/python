#under contruction
#started on 1 dec @5:00pm by nikhil sharma

import random as rm

matrix = []
sudoku_order = int(input("Enter level of sudoku: "))
possible_array = []
entry = ['_','_','_']

for i in range(9):
    for j in range(3):
        matrix.append(entry)

for k in range(9):
    for l in range(3):
        print(matrix[i], end='')
    print('\n')

for possible_entries in range(1, sudoku_order+1):
    possible_array.append(possible_entries)

'''rm.shuffle(possible_array)
matrix.append(possible_array)'''

'''for entry in range(sudoku_order):
    for i in range(sudoku_order):
        entered_val = matrix[0][entry]'''