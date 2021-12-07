#by Nikhil Sharma on 4DEC @6:31pm
#solved LeetCode

def sumCHECK(array, target):
    proof = "notbreak"
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i]+array[j] == target and i != j:
                proof = "break"
                break
            else:
                continue
        if proof == "break":
            break
        else:
            continue
    result = [i,j]
    print(result)

nums = input()  #input list as string
nums = nums.strip('][').split(',')
#nums = list(map(int,input().split()))  #ths is for direct list input
for z in range(0, len(nums)):
    nums[z] = int(nums[z])
target = int(input())

sumCHECK(nums, target)