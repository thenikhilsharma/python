def rookMove(rook_x, rook_y):
    cross = False
    j = rook_y-2
    while j >= 0:
        if chessBoard[rook_x-1][j] != 'R':
            j -= 1
            continue
        else:
            cross = True
            break
    for j in range(rook_y, 8):
        if chessBoard[rook_x-1][j] != 'R':
            continue
        else:
            cross = True
            break
    j = rook_x-2
    while j >= 0:
        if chessBoard[j][rook_y-1] != 'R':
            continue
        else:
            cross = True
            break
        j -= 1
    for j in range(rook_x, 8):
        if chessBoard[j][rook_y-1] != 'R':
            continue
        else:
            cross = True
            break
    if cross == True: print("YES")
    else: print("NO")

t = int(input())
for tc in range(t):
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
    rook1_x, rook1_y, rook2_x, rook2_y = map(int, input().split())
    chessBoard[rook1_x-1][rook1_y-1] = 'R'
    chessBoard[rook2_x-1][rook2_y-1] = 'R'

    rookMove(rook1_x, rook1_y)