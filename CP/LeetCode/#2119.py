#A number after double reversal
#unsolved
# num = input()
# num1 = list(map(str, num))
# num1.reverse()
# num1 = ''.join(num1)
# num1.lstrip('0')
# num1 = list(map(str, num1))
# num1.reverse()
# num1 = ''.join(num1)
# print('true') if num1 == num else print('false')

num = 1800

numstr = str(num)
numstr = numstr.rstrip('0')

return True len(numstr) == len(str(num)) else False