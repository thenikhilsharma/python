N = int(input())    #list length
arr = list(map(int, input().split()))

def check(arr):
    if len(arr) == 1:
        return 0
    else:
        