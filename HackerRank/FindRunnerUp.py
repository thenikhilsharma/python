n = int(input())

arr = list(map(int, input().split()))

arrMAX = max(arr)

c = arr.count(arrMAX)

for i in range(c):
    arr.remove(arrMAX)

arrMAX = max(arr)

print(arrMAX)