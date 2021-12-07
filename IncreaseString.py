t = int(input())
for i in range(t):
    s = input() #input string
    arr = []    #an empty array
    for j in range(len(s)):
        arr.append(s[j])
    arr.sort()
    print(arr)