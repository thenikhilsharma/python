#TEMPLELA
#by Nikhil Sharma on 15 Dec 2021
#@ 3:12 pm incomplete

s = int(input())    #strip length

for sc in range(s):
    def check(arr, n):
        result = "Yes"
        if n%2 == 1:
            if arr[0] == arr[n-1] and arr[0] == 1:
                mid = (n+1) / 2
                mid = int(mid)
                for i in range(mid-1):
                    if arr[i+1] == arr[i] + 1: continue
                    else:
                        result = "No"
                        break
                for i in range(mid, n-1):
                    if arr[i+1] == arr[i] - 1: continue
                    else:
                        result = "No"
                        break
            else: result = "No"
        else: result = "No"
        print(result)
    #function end

    n = int(input())    #length of strip
    arr = list(map(int, input().split()))   #strip height
    check(arr, n)