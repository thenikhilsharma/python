chessBoard = [
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0]
]

king_x, king_y = map(int, input().split())
rook1_x, rook1_y = map(int, input().split())
rook2_x, rook2_y = map(int, input().split())

chessBoard[king_x-1][king_y-1] = 'K'
chessBoard[rook1_x-1][rook1_y-1] = 'R'
chessBoard[rook2_x-1][rook2_y-1] = 'R'

def rookMove(rook_x, rook_y):
    valid_coords= []

    #for y range:
    j = rook_y-2
    while j >= 0:
        if chessBoard[rook_x-1][j] != 'R':
            valid_coords.append([rook_x-1, j])
        else: break
        j -= 1

    for j in range(rook_y, 8):
        if chessBoard[rook_x-1][j] != 'R':
            valid_coords.append([rook_x-1, j])
        else: break
    
    #for x range:
    j = rook_x-2
    while j >= 0:
        if chessBoard[j][rook_y-1] != 'R':
            valid_coords.append([j, rook_y-1])
        else: break
        j -= 1

    for j in range(rook_x, 8):
        if chessBoard[j][rook_y-1] != 'R':
            valid_coords.append([j, rook_y-1])
        else: break

    return valid_coords

def kingMove(king_x, king_y):
    valid_chords = []

    if king_x-1 >= 0: valid_chords.append([king_x-1, king_y])
    if king_x+1 <= 8: valid_chords.append([king_x+1, king_y])
    if king_y-1 >= 0: valid_chords.append([king_x, king_y-1])
    if king_y+1 <= 8: valid_chords.append([king_x, king_y+1])

    return valid_chords

for i in chessBoard:
    print(i)

print("Valid coords of R1 is: ", rookMove(rook1_x, rook1_y))
print("Valid coords of R2 is: ", rookMove(rook2_x, rook2_y))
print("Valid coords of K1 is: ", kingMove(king_x, king_y))