n = int(input())
finalArr = []
arr = []

for z in range(n):
    a = input()
    arr.append(a)
#arr = list(input().split())
res = []

for i in range(len(arr)):
    A = arr.count(arr[i])
    aPercnt = (A/len(arr))*100

    if aPercnt > 5.0:

        for z in arr:
            if z not in res:
                res.append(z)

res.sort()

for k in range(len(res)):
    print(str(res[k]))