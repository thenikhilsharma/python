def oddNums(n):
    if n % 2 != 0: return True
    else: False

nums = [1,2,3,4,5,6,7,8,9]

odds = filter(oddNums, nums)
print(list(odds))

result = filter(lambda n: n % 2 == 0, nums)
print(list(result))