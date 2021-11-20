t = int(input())

def reverse(lst):
    revList = []
    revList.append(lst[N-1])
    revList.append(lst[0])
    finalList=lst
    print(lst)
    for z in range(-N,-1):
        finalList = finalList[:-1:]
        print('appended list',finalList)
        finalList.reverse()
        print('reversed list',finalList)
        revList.append(finalList[0])
        print(revList)

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
    reverse(initialOrder)
    #posCheck(reverse(initialOrder))