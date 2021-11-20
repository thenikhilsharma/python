t = int(input())
for j in range(t):
    n = input()
    def sum(a):
        arr = list(a)
        sum = 0
        for i in range(len(arr)):
            sum = sum + int(arr[i])
        return sum
    print(sum(n))