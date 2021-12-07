#by Nikhil Sharma @6:52pm
#solved
from collections import Counter
from itertools import repeat, chain

def collection(s):
    s.sort()
    s = list(chain.from_iterable(repeat(i, c) for i,c in Counter(s).most_common()))
    count = []

    #aabbbccde
    j = 0
    lst = []
    while j<=len(s)-1:
        z = s[j]
        c = s.count(z)
        count.append(c)
        j += c
        b = [z,c]
        lst.append(b)

    

    for y in range(3):
        print(lst[y][0],end=' ')
        print(lst[y][1],end='\n')

s = input()
arr = []

for i in s:
    arr.append(i)

collection(arr)