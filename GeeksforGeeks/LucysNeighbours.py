'''Lucy lives in house number X. She has a list of N house numbers in the society. Distance between houses can be determined by studying the difference between house numbers. Help her find out K closest neighbors.
Note: If two houses are equidistant and Lucy has to pick only one, the house with the smaller house number is given preference.'''
N, X, K = input().split()
arr = list(map(int, input().split()))

arr.sort()
a = arr.index(N)

for i in range(N):