#by Nikhil Sharma on 19 Nov 2021
#HackerRank

s = input()
lowercase = []
uppercase = []
evendigits = []
odddigits = []
array = []

for i in range(len(s)):
    if s[i].isalpha() and s[i].islower():
        lowercase.append(s[i])
        lowercase.sort()
    elif s[i].isalpha() and s[i].isupper():
        uppercase.append(s[i])
        uppercase.sort()
    elif s[i].isdigit() and int(s[i]) % 2 == 0:
        evendigits.append(s[i])
        evendigits.sort()
    elif s[i].isdigit() and int(s[i]) % 2 != 0:
        odddigits.append(s[i])
        odddigits.sort()

array = lowercase+uppercase+odddigits+evendigits
array = ''.join(array)
print(array)