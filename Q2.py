n = int(input())

arr = []

arr = list(map(int, input().split()))

def check (array):

    N = 0.000000
    P = 0.000000
    Z = 0.000000

    for j in range(n):

        if array[j] > 0:
            P = P + 1.000000
        elif array[j] < 0:
            N = N + 1.000000
        elif array[j] == 0:
            Z = Z + 1.000000
    
    I = float(n)

    x = P/I
    print(round(x, 6))

    y = N/I
    print(round(y, 6))

    z = Z/I
    print(round(z, 6))

check(arr)