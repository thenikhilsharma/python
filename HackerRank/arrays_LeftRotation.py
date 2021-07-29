#28/07/2021 HackerRank 12:48PM

n, d = map(int, input().split())

arr = list(map(int, input().split()))

temp = []

for i in range(d):
    temp.append(arr[i])

del arr[0:d]

arr.extend(temp)

for j in range(len(arr)):
    print(arr[j], end=" ")