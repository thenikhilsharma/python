#by Nikhil Sharma on 11 Dec 2021
#@12:55PM

t = int(input())
for tc in range(t):
    n, m, k = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0

    if arr.count(1) == len(arr): print(100)
    else:
        for i in range(len(arr)):
            if arr[i] == 1:
                cnt += 1
            else: break

        if cnt >= m: print(k)
        else: print(0)