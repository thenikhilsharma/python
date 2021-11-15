#by Nikhil Sharma on 15 Nov 2021

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    arr = []
    for i in range(n):
        if i%3 == 0 and i%5 ==0:
            arr.append(i)
        elif i%3 == 0:
            arr.append(i)
        elif i%5 == 0:
            arr.append(i)
    s = sum(arr)
    print(s)