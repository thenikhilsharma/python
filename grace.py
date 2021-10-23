T = int(input()) #no of test cases
final_arr = []

for i in range(1, T+1):
    K = int(input()) # no of objects
    for j in range(1, K+1):
        arr = list(map(int, input().split()))
        final_arr.append(arr)
    
    #now arr has all the values in it

print(final_arr)