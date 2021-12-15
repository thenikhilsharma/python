#by nikhil sharma on 11 dec 2021
#at 12:47pm

t = int(input())
for tc in range(t):
    n, x, y = map(int, input().split()) #input variables
    n += 1
    team_limit = n * y
    if team_limit < x:
        print("NO")
    else: print("Yes")