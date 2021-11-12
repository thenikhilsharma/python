t = int(input())

def reverse(lst):
    larry = []
    for j in range(N):
        larry.append(lst[j])
        larry.reverse()
        print(larry)
    return larry

def posCheck(arrCheck):
    index = arrCheck.index(K)
    print(index)

for i in range(t):
    initialOrder = []
    arr = list(map(int, input().split()))
    N = arr[0]
    K = arr[1]

    for j in range(N):
        initialOrder.append(j)
    posCheck(reverse(initialOrder))