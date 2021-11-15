q = int(input())

for T in range(q):
    arr = list(map(int, input().split()))
    n = arr[0]
    m = arr[1]

    def f(n):
        n = str(n)
        n = list(n)
        factorial = 1
        factSum = 0

        for j in range(len(n)):
            for i in range(int(n[j])):
                factorial = factorial*i
            factSum = factSum + factorial
        print(factSum)
    f(n)