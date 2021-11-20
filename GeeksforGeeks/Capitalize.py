def solve(s):
    a = s.split()
    for i in a:
        s = s.replace(i,i.capitalize())
    return s

s = input()
result = solve(s)
print(result)