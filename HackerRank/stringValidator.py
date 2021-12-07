#by Nikhil Sharma on 27NOV @7:00pm
#hackerrank sol
#solved

def check(s):
    alpha,num,lower,upper = 0,0,0,0
    for i in range(len(s)):
        if s[i].isalpha():
            alpha = 1
        if s[i].isdigit():
            num = 1
        if s[i].islower():
            lower = 1
        if s[i].isupper():
            upper = 1
    if alpha == 1 or num == 1:
        print("True")
    else:
        print("False")
    if alpha == 1:
        print("True")
    else:
        print("False")
    if num == 1:
        print("True")
    else:
        print("False")
    if lower == 1:
        print("True")
    else:
        print("False")
    if upper == 1:
        print("True")
    else:
        print("False")

if __name__ == '__main__':
    s = input()
    arr = []
    for j in range(len(s)):
        arr.append(s[j])
    check(arr)