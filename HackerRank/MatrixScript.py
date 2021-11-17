#by Nikhil Sharma on 15 Nov 2021
#HackerRank Sol 1HR

import re
inp = list(map(int, input().split()))
N = inp[0]
M = inp[1]

array = []
for i in range(N):
    arr = list(input())
    array.append(arr)

matrix = []
for j in range(M):
    for k in range(N):
        matrix.append(array[k][j])

string = ''.join(matrix)
       
print(re.sub(r'(?<=\w)([^\w\d]+)(?=\w)', ' ', string))