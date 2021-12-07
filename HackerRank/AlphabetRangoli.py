#by nikhil sharma on 1dec
#5:58pm -
from string import ascii_lowercase
N = int(input())

valid_input = []
for c in ascii_lowercase:
    valid_input.append(c)
    if len(valid_input) == N:
        break

rows = 2*N-1
columns = 2*rows-1

print(rows,columns)
for i in range(N):
    for j in range(N):
        pass