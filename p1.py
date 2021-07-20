n = int(input())
arr = []
sumList = []

for i in range(n):
    inp = int(input("", end = " "))
    arr.append(inp)

print(arr)

def summ(array):
    for j in range (0, n, 2):
        summation = arr[j]+arr[j+1]
        sumList.append(summation)
        return sumList

print(summ(arr))