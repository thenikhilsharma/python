# SOLVED
# python program hackerank certificate prg

def common(arri):

    arrSum = 0
    index = []

    index = arri[i-1]

    if index == 0:

        arrSum = arrSum + x

    print(arrSum)

def NOTcommon(arri):

    arrSum = 0
    index = []

    index = arri[i-1:r]

    arrSum = sum(index)

    for y in range (i-1, r):
        if index[y] == 0:
            arrSum = arrSum + x

    print(arrSum)

'''!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'''

n = int(input())

arr = []

for I in range(1, n+1):
    inp = int(input())
    arr.append(inp)

q = int(input())

qe = int(input())

'''!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'''

for z in range(q):

    i, r, x = map(int, input().split())

    X = int(i)
    Y = int(r)

    if i == r:
        common(arr)
    elif i < r:
        NOTcommon(arr)
