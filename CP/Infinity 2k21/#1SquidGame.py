for tc in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    max_prize = sum(arr) - min(arr)
    print(max_prize)