n = int(input())

arr = list(map(int, input().split()))

max = int(max(arr))

no = arr.count(max)

print(no)