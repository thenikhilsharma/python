x = int(input())
n = int(input())

def sExponentSum(x, n):
    sumValue = 0
    for i in range(n+1):
        sumValue = sumValue + x**i
    return sumValue

def aExponentSum(x, n):
    sumValue = 0
    for i in range(n+1):
        if i%2 == 0:
            sumValue = sumValue - x**i
        else:
            sumValue = sumValue + x**i
    return sumValue

def fExponentSum(x, n):
    sumValue = 0
    for i in range(1, n+1):
        if i%2 == 0:
            sumValue = sumValue - (x**i)/i
        else:
            sumValue = sumValue + (x**i)/i
    return sumValue

def afExponentSum(x, n):
    sumValue = 0
    factorial = 1
    for i in range(1, n+1):
        factorial = factorial * i
        if i%2 == 0:
            sumValue = sumValue - (x**i)/factorial
        else:
            sumValue = sumValue + (x**i)/factorial
    return sumValue

print(afExponentSum(x, n))