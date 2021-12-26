#OPTSORT
#by someone else

import heapq as hq
from collections import deque

def solve():
    n = int(input())
    a = list(map(int,input().split()))
    b = sorted(a)
    p = list()
    q = deque()
    ans = 0
    c = -1
    for x, y in zip(a, b):
        if len(q) == 0:
            c = y
        hq.heappush(p, x)
        q.append(y)
        while p and p[0] == q[0]:
            hq.heappop(p)
            q.popleft()
        if len(q) == 0:
            ans += y - c
    print(ans)


def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()

'''for tc in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    cost = 0
    def costfnc(aseg, cost):
        cost += (max(aseg) - min(aseg))
        return cost
    
    sorted_arr = sorted(a)
    change_index = []
    if sorted_arr != a:
        for i in range(n):
            if sorted_arr[i] != a[i]:
                change_index.append(i)
        if len(change_index) == n: cost = costfnc(a, cost)
        else:
            iidx = 0
            fidx = n
            if a[0] != min(a):
                iidx = a.index(min(a))
                segmentarr = a[0:iidx+1]
                segmentarr.sort()
                a = segmentarr + a[iidx+1:]
                cost = costfnc(segmentarr, cost)
            if a[n-1] != max(a):
                fidx = a.index(max(a))
                segmentarr = a[fidx:]
                segmentarr.sort()
                a = a[:fidx] + segmentarr
                cost = costfnc(segmentarr, cost)
            segmentarr = a[iidx:fidx]
            if segmentarr != sorted(segmentarr):
                for i in range(len(segmentarr)):
                    smrt = sorted(segmentarr)
                    if segmentarr[i] == smrt[i]:
                        continue
                    else:
                        start = i
                        break
                for i in range(len(segmentarr)-1,-1,-1):
                    smrt = sorted(segmentarr)
                    if segmentarr[i] == smrt[i]:
                        continue
                    else:
                        end = i
                        break
                segmentarr = segmentarr[start:end+1]
                a = a[:start] + segmentarr + a[end+1:]
                cost = costfnc(segmentarr, cost)
    else: cost = 0
    print(cost)'''