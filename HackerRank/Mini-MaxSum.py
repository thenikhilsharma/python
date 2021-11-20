import math

arr = list(map(int, input().split()))
summation = []
sumi = 0

for i in range(5):
    j = int(arr[i])
    sumi = sum(arr) - j
    summation.append(sumi)

print(max(summation), end=" ")
print(min(summation))