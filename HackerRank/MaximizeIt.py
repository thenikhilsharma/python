#unsolved
#by Nikhil Sharma on 15 Nov 2021
#HackerRank on 9:54PM

inp = list(map(int, input().split()))
K = inp[0]
M = inp[1]

array = []
for i in range(K):
    arr = list(map(int, input().split()))
    amax = max(arr)
    amax = amax**2
    print(amax)
    array.append(amax)

sum = sum(array)
mod = sum%M
print(mod)
