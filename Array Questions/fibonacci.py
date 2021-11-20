n = int(input("Enter the number: "))

def fibonacciSeries(n):
    i = 0
    n1, n2 = 0, 1
    fib = 0

    while i <= n:
        print(n1, end=" ")
        j = n1+n2
        n1 = n2
        n2 = j
        i = i+1

fibonacciSeries(n)