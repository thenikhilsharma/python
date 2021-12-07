nums = list(map(int, input("nums = ").split()))
target = int(input())

print(nums, target)

for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i]+nums[j] == target:
            print(nums[i],nums[j])