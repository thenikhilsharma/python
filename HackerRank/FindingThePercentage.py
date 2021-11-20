#by Nikhil Sharma on 15 Nov 2021
#HackerRank

t = int(input())
array = []

for i in range(t):
    arr = list(input().split())
    array.append(arr)

name = input()

for j in range(t):
    if str(array[j][0]) == name:
        if array[j][1].isdigit():
            a1 = int(array[j][1])
        else:
            a1 = float(array[j][1])
        if array[j][2].isdigit():
            a2 = int(array[j][2])
        else:
            a2 = float(array[j][2])
        if array[j][1].isdigit():
            a3 = int(array[j][3])
        else:
            a3 = float(array[j][3])

        s = (a1+a2+a3)/3
        s = "{:.2f}".format(s)
        print(s)