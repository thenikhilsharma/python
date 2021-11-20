'''binary numbers hacker rank 30days challenge
12 Nov 2021
by Nikhil Sharma'''

n = int(input())
arr = bin(n).replace("0b", "")

arr = list(arr)
streakArr = []
streak = 0
for i in range(len(arr)):
    if int(arr[i]) == 1:
        streak = streak+1
    elif int(arr[i]) == 0:
        streakArr.append(streak)
        streak = 0
streakArr.append(streak)

print(streakArr)