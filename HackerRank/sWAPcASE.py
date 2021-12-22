def swap_case(s):
    s = list(s)
    arr = []
    for i in range(len(s)):
        s[i] = str(s[i])
        if s[i].isupper():
            arr.append(s[i].lower())

        elif s[i].islower():
            arr.append(s[i].upper())
        else:
            arr.append(s[i])
            pass
    arr = ''.join(arr)
    return arr

s = input()
result = swap_case(s)
print(result)