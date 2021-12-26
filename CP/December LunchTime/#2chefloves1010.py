#CHEF1010

for tc in range(int(input())):
    n = int(input())
    a = input()
    a = list(map(str, a))
    s1 = a.count('1')
    s0 = a.count('0')
    if s1 < s0 : s0 = s1
    elif s0 < s1 : s1 = s0
    elif s1 == s0 : pass
    print(s1-1) if s1 > 0 else print(0)