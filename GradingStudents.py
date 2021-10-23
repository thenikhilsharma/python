'''TheNikhilSharma
Date - 23 Oct 2021
Time - 2:03(finishing time)
Attempts - 6-7
Program Name - Grading Students (Hacker Rank)'''

t = int(input())

for i in range (t):
    score = int(input())

    if score>=0 and score <=100:

        x = score%5
        if x>0:
            y = 5-x
        else:
            y=x
            print(score)

        nextMultiple = score+y

        if score >= 38 and x!=0:
            if nextMultiple > score:
                z = nextMultiple - score
                if z < 3:
                    print(nextMultiple)
                elif z == 3:
                    print(score)
                elif z > 3:
                    print(score)
        elif score<38 and x!=0:
            print(score)