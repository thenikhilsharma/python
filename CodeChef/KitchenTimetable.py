#KTTABLE
#by Nikhil Sharma on 17Dec

t = int(input())
for tc in range(t):
    n = int(input())    #no of students
    time_alloted = list(map(int, input().split()))
    time_req = list(map(int, input().split()))

    def willAble (givenTime, reqTime):
        willCook = 0
        for i in range(len(givenTime)):
            if i != 0: time = givenTime[i] - givenTime[i-1]
            else: time = givenTime[i]
            if time >= reqTime[i]: willCook += 1
            else: continue
        return willCook
    
    print(willAble(time_alloted, time_req))