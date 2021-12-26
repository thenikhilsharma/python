#time limit exceeded in one tc
#RMNTREV

for ct in range(int(input())):
    n, k = map(int, input().split())
    sdash = input()
    sub_string = list(sdash[0:k])
    sub_string2 = list(sdash[k:])
    
    for i in range(k):
        sub_string.reverse()
        temp = sub_string[len(sub_string)-1]
        sub_string2.insert(0,temp)
        del sub_string[len(sub_string)-1]

    ans = ''.join(sub_string2)
    print(ans)