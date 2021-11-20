n = int(input())        # Enter no. of elements to enter

arr = []                # creating an empty array

arr = list(map(int, input().split()))   # input array

def check (array):                      # function to check array

    N = 0.0
    P = 0.0
    Z = 0.0

    for j in range(n):

        if array[j] > 0:
            P = P + 1.0
        elif array[j] < 0:
            N = N + 1.0
        elif array[j] == 0:
            Z = Z + 1.0
    
    I = float(n)

    x = P/I
    X = round(x, 6)
    print(format(X, '0.6f'))

    y = N/I
    Y = round(y, 6)
    print(format(Y, '0.6f'))

    z = Z/I
    Z = round(z, 6)
    print(format(Z, '0.6f'))

check(arr)