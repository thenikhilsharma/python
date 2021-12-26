#SLEEPTECH
#solved by another

import sys
readline = sys.stdin.readline

ns = lambda: readline().rstrip()
ni = lambda: int(readline().rstrip())
nm = lambda: map(int, readline().split())
nl = lambda: list(map(int, readline().split()))

def solve():
    n, a, b = nm()
    lr = [tuple(nm()) for _ in range(n)]
    event = [(l, 1) for l, r in lr] + [(r+1, -1) for l, r in lr] + [(10**20, 0)]
    event.sort()
    ans = cur = 0
    bef = 0
    for t, v in event:
        l, r, c = bef, t-1, cur
        bef = t
        cur += v
        if ans >= c:
            continue
        ok = 0
        ng = b - a + 2
        while ng - ok > 1:
            mid = (ok + ng) // 2
            if (b + b - mid + 1) * mid // 2 < l:
                ok = mid
            else:
                ng = mid
        # print((l, r), cur, ok, ((b + b - ok + 1) * ok // 2, (a + a + ok) * (ok + 1) // 2))
        if ok < b - a + 1 and (a + a + ok) * (ok + 1) // 2 <= r:
            # print("OK")
            ans = c

    print(ans)


def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()