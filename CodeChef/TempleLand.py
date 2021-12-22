#TEMPLELA
#by Nikhil Sharma on 15 Dec 2021
#@ 11:31 pm complete

s = int(input())    #strip length

for sc in range(s):
    def check(arr, n):
        result = "Yes"
        if n%2 == 0: result = "No"
        else:
            start, end, counter = 0, n-1, 1
            while start <= end:
                if arr[start] != counter or arr[end] != counter:
                    result = "No"
                    break
                start += 1
                end -= 1
                counter += 1
        print(result)
    #function end

    n = int(input())    #length of strip
    arr = list(map(int, input().split()))   #strip height
    check(arr, n)

##################################################################
#earlier solution
##################################################################
#TEMPLELA
#by Nikhil Sharma on 15 Dec 2021
#@ 3:12 pm complete
'''
s = int(input())    #strip length
for sc in range(s):

    def check(arr, n):
        result = "yes"
        if n%2 == 1:
            if arr[0] == arr[n-1] and arr[0] == 1:
                mid = (n+1) / 2
                mid = int(mid)
                for i in range(mid-1):
                    if arr[i+1] == arr[i] + 1: continue
                    else:
                        result = "no"
                        break
                for i in range(mid, n-1):
                    if arr[i+1] == arr[i] - 1: continue
                    else:
                        result = "no"
                        break
            else: result = "no"
        else: result = "no"
        print(result)
    #function end

    n = int(input())    #length of strip
    arr = list(map(int, input().split()))   #strip height
    check(arr, n)
'''