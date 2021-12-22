#DECODEIT
#by Nikhil Sharma on 19 dec @ 8:00PM

t = int(input())
for tc in range(t):
    n = int(input())    #length of string
    s = input()         #string
    allLetter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
    
    def decode(s, x, string, i):
        if len(string) == 1:
            return string[0]
        else:
            half = int(len(string) / 2)
            halfStringLeft = string[0:half]
            halfStringRight = string[half:]
            if half == 1:
                if x == '0':
                    return decode(s, s[i], halfStringLeft, i)
                else:
                    return decode(s, s[i], halfStringRight, i)
            else:
                if x == '0':
                    return decode(s, s[i+1], halfStringLeft, i+1)
                else:
                    return decode(s, s[i+1], halfStringRight, i+1)
    lastpos = 0
    sub_split = []
    if len(s) == 4:
        print(decode(s, s[0], allLetter, 0))
    else:
        for j in range(4, len(s)+1, 4):
            sub_split.append(s[lastpos:j])
            lastpos += j
        for j in sub_split:
            print(decode(j, j[0], allLetter, 0), end='')
        print('')