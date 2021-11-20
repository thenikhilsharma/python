factorial = 1

n = int(input("Enter any Number to get factorial of it: "))

def calcfactorial(factorial):
    for i in range(1, n+1):
        factorial = factorial * i

    return factorial

print(calcfactorial(factorial))