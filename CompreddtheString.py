s = input()
s = list(s)

sr= []
p= 0
for i in range(len(s)):
    for j in range(i, len(s)):
        if s[i] == s[j]:
            p += 1
        else:
            sr.append(p)
            break
        if i == j and i == len(s) - 1:
            sr.append(p)

print(sr)